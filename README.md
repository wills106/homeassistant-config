[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/V7V51QQOL)
Don't feel like you have to Donate, I have only added it due to requests.

# Home Assistant Configuration

My [Home Assistant](https://home-assistant.io/) Configuration Files

## Version

[.HA_VERSION](https://github.com/wills106/homeassistant-config/blob/master/.HA_VERSION)

## Screen Shots

Screen Shots giving an idea of the Lovelace UI - will change quite a bit as I get it better organised.

[Screen Shots](https://github.com/wills106/homeassistant-config/blob/master/screenshots/README.md)

## Devices

I am now running Supervisor (HASSIO) with the [Synology native Package](https://community.home-assistant.io/t/hass-io-on-synology-dsm-native-package/125559)
Previously I was running HASSIO as a Virtual Machine on my Synology DS918+ this replaced an older Docker Version running on a DS1511+ Synology.

- Synology DS918+
- 6x WD 8TB "External drives removed / lots cheaper!" ( Yes I know the DS918+ is meant to "only have" 4 bays )
- pfSense  Firewall / Router running on an Intel 3865u 6 NIC Mini PC
- Ubiquiti US-16-150W 16 Poprt PoE Managed Switch
- Ubiquiti UniFi nanoHD Access Point
- XIAOMI Roborock Vacuum Cleaner Gen 2 Rooted and running [Valetudo](https://github.com/Hypfer/Valetudo)

### The following are flashed with [Tasmota Firmware](https://github.com/arendst/Sonoff-Tasmota)
I use [Tuya-Convert](https://github.com/ct-Open-Source/tuya-convert) to flash new devices over the air (OTA)
- Sonoff RF 433 - WiFi Bridge
- Sonoff Basic WiFi Relay
- Sonoff 4CH Pro R2
- Tuya Dimmer Switch 1 Gang
- Sonoff T1 WiFi Wall Switch 1 Gang
- Sonoff T1 WiFi Wall Switch 2 Gang
- Sonoff T1 WiFi Wall Switch 3 Gang
- Magichome Wifi LED Strip Light Controller
- LOHAS GU10 RGB
- TECKIN Smart WiFi Plug
- 4 Way Powerstrip Manzoku / ZLD-44UK-W
- 2 Gang UK Wall Stockets

### Z-Wave Devices
- Z-WAVE.ME ZMEEUZB1 Z-Wave USB dongle
- Eurotronic SPIRIT Z-Wave TRV
- Yale Conexis L1 Smart Lock
- Yale Z-Wave Module 2

### Security

- HikVision DS-2CD2T42WD-I5
- HikVision DS-2CD2T42WD-I8
- HiWatch DB-120A-IW WiFi Smart Doorbell ( HikVision Version DS-KB6403-WIP )
- KERUI D026 RF Door/Window Sensor
- KERUI P829 RF Motion Sensor

### Solar

- SolaX X1-Hybrid-5.0-D-E (Gen3)
- 1 x SolaX Gen2 Tripple Power HV 4.5kWh battery
- 16 x JA Solar 305w PV Panels

## Retired Devices
- Synology DS1511+ (Docker running Home Assistant)
- Linksys WRT1900ACS Router
