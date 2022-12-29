# WTCL Code

A collection of scripts that help automate proccesses in the Discord racing team management game, _World Touring Car League_ which runs on rFactor.

Join WTCL here:
https://disboard.org/server/946893614808723496

Note: Some changes have been effected in the WTCL Hub Cheatsheet, which is only available to Board Members

## Todo

- Excel-based generation of all files, replacing `generate_combined.py` and `generate_veh.py`. Both files are considered deprecated.
- Implement `click` for `timestamp`

## Generate upgrades

Reads from the hub cheatsheet and calls on `generate_hdv` and `generate_engine_ini` accordingly.

```
python generate_upgrades.py --race=r5
```

```
Options:
  --race TEXT  round number for upgrades
  --help       Show this message and exit.
```

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

## Update fanbase

Updates a team's fanbase count (and thus affecting merchandise sales) for the next WTCL season.

```
python generate_merchandise.py --base=100000 --rep=75 --series=itcl
```

```
Options:
  --base TEXT    team fanbase
  --rep TEXT     team reputation
  --series TEXT  series (e.g ITCL, WTCL)
  --help         Show this message and exit.
```

## Generate hdv

Adjusts the weight, drag and aero coefficients to the corresponding to the respective vehicle upgrades.

```
python generate_hdv.py --team=astra --model=egl --ce=6 --aero=1 --drag=0 --weight=0
```

```
Options:
  --team TEXT    team shorthand
  --model TEXT   car model
  --ce TEXT      chief engineer effect
  --aero TEXT    body aero value
  --drag TEXT    body drag value
  --weight TEXT  weight reduction value
  --help         Show this message and exit.
```

Files can be found in the `itcl/` or `wtcl/` directory.


## Generate engine files

Creates an .ini file from reliability upgrades information. Enter the upgrades as negative if they fail to make the activity check too.

```
python generate_engine_ini.py --team=astra --series=itcl --ce=6 --rel=3
```

```
Options:
  --team TEXT          team shorthand
  --series TEXT        series (e.g ITCL, WTCL)
  --ce TEXT            chief engineer effect
  --num_upgrades TEXT  reliability level
  --help               Show this message and exit.
```

Files can be found in the `itcl/` or `wtcl/` directory.

## Mods

Works for the [V8FU](https://www.racedepartment.com/downloads/v8factor-unleashed-part-one.49297/) and the [ITCC 2013](https://www.rfactorcentral.com/detail.cfm?ID=ITCC%202013) mods.