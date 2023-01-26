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
        ce = int(row['ce'])
        upgrades = row[race].split(',')
        if clasS == 'wtcl':
            aero = int(upgrades[0])
            drag = int(upgrades[1])
            weight = int(upgrades[2])
            rel = int(upgrades[3])
        else:
            aero = int(upgrades[0])
            weight = int(upgrades[1])
            rel = int(upgrades[2])
            drag = None
        generate_hdv.generate_hdv(team_short, car, ce, aero, drag, weight)
        generate_engine_ini.generate_engine_ini(team_short, clasS, ce, rel)

if __name__ == '__main__':
    loadUpgrades()