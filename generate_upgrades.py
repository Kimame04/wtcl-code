import generate_engine_ini, generate_hdv
import click
import pandas as pd

@click.command()
@click.option('--race', help="round number for upgrades")

def loadUpgrades(race):
    excel_file = pd.ExcelFile('hub-cheatsheet.xlsx')
    df = excel_file.parse('upgrades')
    for index, row in df.iterrows():
        team_short = row['shorthand']
        car = row['car']
        clasS = row['series']
        ce_multiplier = int(row['ce']) * 0.01 + 1
        upgrades = row[race].split(',')
        if clasS == 'wtcl':
            aero = int(upgrades[0])
            drag = int(upgrades[1])
            rel = int(upgrades[2])
            weight = int(upgrades[3])
        else:
            aero = int(upgrades[0])
            weight = int(upgrades[1])
            rel = int(upgrades[2])
            drag = None
        generate_engine_ini.generate_engine_ini(team_short, clasS, ce_multiplier, rel)
        generate_hdv.generate_hdv(team_short, car, ce_multiplier, aero, drag, weight)

if __name__ == '__main__':
    loadUpgrades()