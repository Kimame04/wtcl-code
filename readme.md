# WTCL Code

A collection of scripts that help automate proccesses in the Discord racing team management game, _World Touring Car League_ which runs on rFactor.

Join WTCL here:
https://disboard.org/server/946893614808723496

## Generate drivers

Execute `generate_drivers.py`.

Randomises driver's age, nationality, stats.

WIP: Handle youth drivers

## Generate driver rcd

Execute `generate_rcd.py`.

Generates driver talent files from an excel of drivers, taken from the WTCL hub. Updated quarterly with the driver improvements.

## Generate hdv

Execute `generate_hdv.py`. 

Adjusts the weight, drag and aero coefficients to the corresponding to the respective vehicle upgrades.

Works for the [V8FU](https://www.racedepartment.com/downloads/v8factor-unleashed-part-one.49297/) and the [ITCC 2013](https://www.rfactorcentral.com/detail.cfm?ID=ITCC%202013) mods.

## Generate veh

Execute `generate_veh.py`.

Creates the .veh file which accompanies a livery .dds file. Contains livery, vehicle, team and driver information.