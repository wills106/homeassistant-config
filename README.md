[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/V7V51QQOL)
Don't feel like you have to Donate, I have only added it due to requests.

[Octopus.Energy 🐙](https://share.octopus.energy/wise-boar-813) referal code. You get £50 credit for joining and I get £50 credit.

# Home Assistant Configuration

My [Home Assistant](https://home-assistant.io/) Configuration Files

## Version

[HA_VERSION](https://github.com/wills106/homeassistant-config/blob/master/HA_VERSION)

## Screen Shots

Screen Shots giving an idea of the Lovelace UI - will change quite a bit as I get it better organised. (09 April 2021 Update - Very outdated)

[Old Screen Shots](https://github.com/wills106/homeassistant-config/blob/master/screenshots/README.md)

Powerflow card and myEnergi sensors for solar diversion and EV Charger.

![PowerCard](https://github.com/wills106/homeassistant-config/blob/master/screenshots/energy.PNG)

## Devices

I was previously running Supervisor (HASSIO) with the [Synology native Package](https://community.home-assistant.io/t/hass-io-on-synology-dsm-native-package/125559)
Prior to that I was running HASSIO as a Virtual Machine on my Synology DS918+ this replaced an older Docker Version running on a DS1511+ Synology.

Now I am running Supervisior (HASSIO) on top of Debian running on a J4125 NUC Type device, while I determin where my installation should live long term.

- Synology DS918+ NAS (Sort off)
- 6x WD 8TB "External drives removed / lots cheaper!" ( Yes I know the DS918+ is meant to "only have" 4 bays )
- pfSense  Firewall / Router running on an Intel 3865u 6 NIC Mini PC
- Ubiquiti US-16-150W 16 Poprt PoE Managed Switch
- Ubiquiti UniFi nanoHD Access Point
- XIAOMI Roborock Vacuum Cleaner Gen 2 Rooted and running [Valetudo](https://github.com/Hypfer/Valetudo)

### I have migrated most ESP Based devices over from [Tasmota Firmware](https://github.com/arendst/Sonoff-Tasmota) to [ESPHome](https://esphome.io/)
I use [Tuya-Convert](https://github.com/ct-Open-Source/tuya-convert) to flash new devices over the air (OTA)
- Sonoff RF 433 - WiFi Bridge - Still on Tasmota
- Sonoff Basic WiFi Relay
- Sonoff 4CH Pro R2
- Tuya Dimmer Switch 1 Gang - Still on Tasmota
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

I have replaced the Synology Surveillance Station with [Frigate](https://github.com/blakeblackshear/frigate) this is using a [Google Coral](https://coral.ai/products/accelerator) USB stick for object based motion detection. Person, Car (Automobile), Cat's, Dog's etc
I plan on running [DeepStack](https://docs.deepstack.cc/) On a [Nvidia Jetson Nano 4GB Dev Kit](https://www.nvidia.com/en-gb/autonomous-machines/embedded-systems/jetson-nano/) for Face Recognition based on motion events provided by [Frigate](https://github.com/blakeblackshear/frigate).
- 2 x HikVision DS-2CD2386G2-IU
- HikVision DS-2CD2T42WD-I5
- HikVision DS-2CD2T42WD-I8
- HiWatch DB-120A-IW WiFi Smart Doorbell ( HikVision Version DS-KB6403-WIP )
- KERUI D026 RF Door/Window Sensor
- KERUI P829 RF Motion Sensor

### Solar - Energy

- [SolaX X1-Hybrid-5.0-D-E (Gen3)](https://www.solaxpower.com/single-phase-hybrid/)
- 2 x [SolaX Gen2 Tripple Power HV 4.5kWh battery](https://www.solaxpower.com/triple-power-battery/)
- 16 x JA Solar 305w PV Panels
- EV Charger [Zappi v2](https://myenergi.com/product/zappi/)
- Solar Diverter [Eddi](https://myenergi.com/product/eddi/) for immersion heater

## Retired Devices
- Synology DS1511+ (Docker running Home Assistant)
- Linksys WRT1900ACS Router
