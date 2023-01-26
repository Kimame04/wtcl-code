# WTCL Code

A collection of scripts that help automate proccesses in the Discord racing team management game, _World Touring Car League_ which runs on rFactor.

Join WTCL here:
https://disboard.org/server/946893614808723496

Note: Some changes have been effected in the WTCL Hub Cheatsheet, which is only available to Board Members

## Todo

- Implement `click` for `timestamp`
- Support for WTCCEX and Clio Cup mods

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

## Generate talent files

```
python generate_talent.py --season=s6-1
```

```
Options:
  --season TEXT  [season number]-[half]
  --help         Show this message and exit.
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

## Generate GDB section

Creates section of a .gdb file to paste into the track .gdb file, thus creating a pre-set grid. More info on this in [this](http://angelodeasa.blogspot.com/2010/11/rfactor-misc-starting-grid-editing-part.html?m=1) article.

```
python generate_gdb_section.py --series=wtcl --filename=test.xlsx --pname=kimame_04
```

```
Options:
  --series TEXT    itcl or wtcl?
  --filename TEXT  name of excel file with quali order
  --pname TEXT     name of player in rFactor (e.g alexis, proba123)
  --help           Show this message and exit.
```

## Mods

Works for the [V8FU](https://www.racedepartment.com/downloads/v8factor-unleashed-part-one.49297/) and the [ITCC 2013](https://www.rfactorcentral.com/detail.cfm?ID=ITCC%202013) mods.