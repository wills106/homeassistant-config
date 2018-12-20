from datetime import timedelta
import logging
import voluptuous as vol

from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (CONF_USERNAME, CONF_PASSWORD, CONF_PLATFORM)
from homeassistant.helpers import discovery
from homeassistant.helpers.dispatcher import (
    dispatcher_send, async_dispatcher_connect)
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.event import track_time_interval

_LOGGER = logging.getLogger(__name__)

REQUIREMENTS = ['meross_iot==0.1.2.0']

DOMAIN = 'meross'
DATA_MEROSS = 'data_meross'
DATA_DEVICES = 'data_devices'

SIGNAL_DELETE_ENTITY = 'meross_delete'
SIGNAL_UPDATE_ENTITY = 'meross_update'

SERVICE_FORCE_UPDATE = 'force_update'
SERVICE_PULL_DEVICES = 'pull_devices'

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_PASSWORD): cv.string,
        vol.Required(CONF_USERNAME): cv.string,
    })
}, extra=vol.ALLOW_EXTRA)


def setup(hass, config):
    """Set up Tuya Component."""
    from meross_iot.api import MerossHttpClient

    username = config[DOMAIN][CONF_USERNAME]
    password = config[DOMAIN][CONF_PASSWORD]

    meross = MerossHttpClient(email=username, password=password)
    hass.data[DATA_MEROSS] = meross
    hass.data[DOMAIN] = {
        'entities': {}
    }

    def load_devices():
        hass.data[DATA_DEVICES] = {}
        for device in meross.list_supported_devices():
            hass.data[DATA_DEVICES][device.device_id()] = device

        """Load new devices by device_list."""
        device_type_list = {}
        for device in hass.data[DATA_DEVICES].values():
            if device.device_id() not in hass.data[DOMAIN]['entities']:
                ha_type = 'switch'
                if ha_type not in device_type_list:
                    device_type_list[ha_type] = []
                device_type_list[ha_type].append(device.device_id())
                hass.data[DOMAIN]['entities'][device.device_id()] = None
        for ha_type, dev_ids in device_type_list.items():
            discovery.load_platform(
                hass, ha_type, DOMAIN, {'dev_ids': dev_ids}, config)

    load_devices()

    def poll_devices_update(event_time):
        """Check if accesstoken is expired and pull device list from server."""
        _LOGGER.debug("Pull devices from Meross.")
        # Add new discover device.
        load_devices()
        # Delete not exist device.
        for dev_id in list(hass.data[DOMAIN]['entities']):
            if dev_id not in hass.data[DATA_DEVICES].keys():
                dispatcher_send(hass, SIGNAL_DELETE_ENTITY, dev_id)
                hass.data[DOMAIN]['entities'].pop(dev_id)

    track_time_interval(hass, poll_devices_update, timedelta(minutes=15))

    hass.services.register(DOMAIN, SERVICE_PULL_DEVICES, poll_devices_update)

    def force_update(call):
        """Force all devices to pull data."""
        dispatcher_send(hass, SIGNAL_UPDATE_ENTITY)

    hass.services.register(DOMAIN, SERVICE_FORCE_UPDATE, force_update)

    return True


class MerossDevice(Entity):
    """Meross base device."""

    def __init__(self, id):
        """Meross devices."""
        self.id = id

    async def async_added_to_hass(self):
        """Call when entity is added to hass."""
        dev_id = self.id
        self.hass.data[DOMAIN]['entities'][dev_id] = self.entity_id
        async_dispatcher_connect(
            self.hass, SIGNAL_DELETE_ENTITY, self._delete_callback)
        async_dispatcher_connect(
            self.hass, SIGNAL_UPDATE_ENTITY, self._update_callback)

    @property
    def device_id(self):
        """Return Meross device id."""
        return self.id

    @property
    def unique_id(self):
        """Return a unique ID."""
        return 'meross.{}'.format(self.id)

    @property
    def name(self):
        """Return Meross device name."""
        return self.id

    @property
    def available(self):
        """Return if the device is available."""
        return True

    def update(self):
        """Refresh Tuya device data."""
        None

    def device(self):
        return self.hass.data[DATA_DEVICES][self.id]

    @callback
    def _delete_callback(self, dev_id):
        """Remove this entity."""
        if dev_id == self.device_id:
            self.hass.async_create_task(self.async_remove())

    @callback
    def _update_callback(self):
        """Call update method."""
        self.async_schedule_update_ha_state(True)