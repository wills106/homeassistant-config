from homeassistant.components.switch import ENTITY_ID_FORMAT, SwitchDevice
from ..meross import DATA_DEVICES, MerossDevice


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up Meross Switch device."""
    if discovery_info is None:
        return
    meross_devices = hass.data[DATA_DEVICES]
    dev_ids = discovery_info.get('dev_ids')
    devices = []
    for dev_id in dev_ids:
        if meross_devices[dev_id] is not None:
            devices.append(MerossSwitch(dev_id))
    add_entities(devices)


class MerossSwitch(MerossDevice, SwitchDevice):
    """meross Switch Device."""

    def __init__(self, id):
        """Init Meross switch device."""
        super().__init__(id)
        self.entity_id = ENTITY_ID_FORMAT.format(id)

    @property
    def is_on(self):
        """Return true if switch is on."""
        if self.device() is None:
            return False
        return self.device().get_status()

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self.device() and self.device().turn_on()

    def turn_off(self, **kwargs):
        """Turn the device off."""
        self.device() and self.device().turn_off()