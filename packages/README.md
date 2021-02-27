How to use [Packages](https://www.home-assistant.io/docs/configuration/packages/)

I have some example Lovelace views in the lovelace-example folder.

[myengeri.yaml](https://github.com/wills106/homeassistant-config/blob/master/packages/myengeri.yaml) Read the Status of myEnergi Eddi & Zappi2.0

SolaX Inverter versions:

[solax_x1ac.yaml](https://github.com/wills106/homeassistant-config/blob/master/packages/solax_x1ac.yaml) is formatted for the X1-AC with SolaX Triple Power Batteries and defaulting to ModBus over RS485.

[solax_x1_hybrid_g2_pylontech.yaml](https://github.com/wills106/homeassistant-config/blob/master/packages/solax_x1_hybrid_g2_pylontech.yaml) is formatted for the Gen 2 with PylonTech Batteries, as the charge rate and some values off-sets are different to the newer Gen3 with SolaX Triple Power batteries. Thanks to @matthewjporter for help with the scaling.

[solax_x1_hybrid_g3_triplepower.yaml](https://github.com/wills106/homeassistant-config/blob/master/packages/solax_x1_hybrid_g3_triplepower.yaml) is formatted for the Gen 3 with SolaX Triple Power Batteries.

[solax_x3_hybrid_g3_triplepower.yaml](https://github.com/wills106/homeassistant-config/blob/master/packages/solax_x3_hybrid_g3_triplepower.yaml) is formatted for the 3-Phase Gen 3 with SolaX Triple Power Batteries also include the full known list of registers, possible not all registers will return values..
