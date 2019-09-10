# Adopting 123's (Taras) on community.home-assistant.io method of Strategy 2: Demultiplexer for RF Codes
# https://community.home-assistant.io/t/sonoff-rf-bridge-strategies-for-receiving-data/108181
# Simplifies RF Sensors and their automations and if you don't publish this file on your GitHub,
# you can keep your RF Codes to your self!
# Sensor 1 - Master Bedroom Window
# Sensor 2 - Master Bedroom Window Alarm
# Sensor 3 - Front Door
# Sensor 4 - Front Door Alarm
# Sensor 5 - Rear Door
# Sensor 6 - Rear Door Alarm
d = { '1234EE':['sensor1','ON','true'],
      '1234E7':['sensor1','OFF','true'],
      '1234EB':['sensor2','ON','false'],
      '1235EE':['sensor3','ON','true'],
      '1235E7':['sensor3','OFF','true'],
      '1235EB':['sensor4','ON','false'],
      '1236EE':['sensor5','ON','true'],
      '1236E7':['sensor5','OFF','true'],
      '1236EB':['sensor6','ON','false']
    }

p = data.get('payload')

if p is not None:
  if p in d.keys():
    service_data = {'topic':'home/{}'.format(d[p][0]), 'payload':'{}'.format(d[p][1]), 'qos':0, 'retain':'{}'.format(d[p][2])}
  else:
    service_data = {'topic':'home/unknown', 'payload':'{}'.format(p), 'qos':0, 'retain':'false'}
    logger.warning('<rfbridge_demux> Received unknown RF command: {}'.format(p))
  hass.services.call('mqtt', 'publish', service_data, False)