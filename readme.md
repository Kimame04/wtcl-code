# WTCL Code

A collection of scripts that help automate proccesses in the Discord racing team management game, _World Touring Car League_ which runs on rFactor.

Join WTCL here:
https://disboard.org/server/946893614808723496

## Todo

- generate_combined for all teams (useful in pre-season)
- youth driver improvements
- merchandise sales code

## Generate hdv, engine and veh files

```
python generate_combined.py
```

All-in-one file generation for a single team. The .veh files reference the .hdv and the engine.ini files, so depending on team parameters all are generated together.

Example:

```
team code: astra
team name: Astra Racing Team
model code: egl
class: itcl
Enter driver 1 name, number, contract: Syd Van Der Linde,31,ft
Enter driver 2 name, number, contract: Carlos Ramirez,32,ft
Enter driver 3 name, number, contract: Kiril Despodov,33,rumble
chief engineer effect (in %): 6
reliability upgrades: 2
```

Files can be found in the `itcl/` or `wtcl/` directory.

## Generate a driver

```
python generate_drivers.py
```

Randomises a new driver's age, nationality, stats.

## Generate driver rcd

```
python generate_rcd.py
```

Generates all driver talent files from an excel of drivers, taken from the WTCL hub. Updated every half season with the driver improvements.

Files can be found in the `drivers/` directory.

## Generate hdv

```
python generate_hdv.py
```

Adjusts the weight, drag and aero coefficients to the corresponding to the respective vehicle upgrades.

Examples:

```
team: astra
model code: egl
chief engineer effect (in %): 6
upgrades, separate commas: 1,0
```

```
team: ester 
model code: fg
chief engineer effect (in %): 9
upgrades, separate commas: 2,4,6
```

Files can be found in the `itcl/` or `wtcl/` directory.

## Generate veh

```
python generate_veh.py
```

Creates the .veh file which accompanies a livery .dds file. Contains livery, vehicle, team and driver information.

Example:

```
Enter short team name: astra
Enter long team name: Astra Racing Team
Enter model: egl
Enter driver 1 name, number, contract: Syd Van Der Linde,31,ft
Enter driver 2 name, number, contract: Carlos Ramirez,32,ft
Enter driver 3 name, number, contract: Kiril Despodov,33,rumble
```

Files can be found in the `itcl/` or `wtcl/` directory.

## Generate engine files

```
python generate_engine_ini.py
```

Creates an .ini file from reliability upgrades information. Enter the upgrades as negative if they fail to make the activity check too.

Examples:

```
team: astra
class: itcl
chief engineer effect (in %): 6
reliability upgrades: 3
```

```
team: astra
class: itcl
chief engineer effect (in %): 6
reliability upgrades: -1
```

Files can be found in the `itcl/` or `wtcl/` directory.

## Mods

Works for the [V8FU](https://www.racedepartment.com/downloads/v8factor-unleashed-part-one.49297/) and the [ITCC 2013](https://www.rfactorcentral.com/detail.cfm?ID=ITCC%202013) mods.