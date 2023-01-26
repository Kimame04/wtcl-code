import unicodedata
import click
import pandas as pd

@click.command()
@click.option('--season', help="[season number]-[half]")

def generate_veh(season):

    sounds = {'chr': 'sonidos', 'css': 'sonidos', 'egl': 'sonidos3', 'mts': 'sonidos3', 'rnl': 'sonidos4', 'fg': 'FG', 've': 'VE'}
    models = {'chr': 'chrysler', 'css': 'bentley', 'egl': 'eagle', 'mts': 'mitsubishi', 'rnl': 'renault', 'fg': 'Ford FG', 've': 'Holden VE'}
    divisions = {'1': 'wtcl', '2': 'itcl'}
    roles = {"full time": 'FT', 'rumble': 'RUMBLE'}

    excel_file = pd.ExcelFile('hub-cheatsheet.xlsx')
    df = excel_file.parse(f'drivers-{season}-ny')
    for index, row in df.iterrows():
        name = unicodedata.normalize('NFD', str(row['Name'])).encode('ascii', 'ignore').decode()
        clasS = divisions[str(int(row["Div"]))]
        team_short = row["team_short"]
        model = row["model"]
        team_long = row["Team"]
        num = int(row["No."])
        role = roles[row["Role"].strip().lower()].upper()
        with open(f"{clasS}/{team_short}_{num}.veh", 'w') as f:
            if clasS == 'itcl':
                f.write(
                    f"defaultLivery={team_short}_{num}.dds"
                    f"\nHDVehicle={team_short}.hdv"
                    f"\nGraphics={models[model]}_gen.gen"
                    f"\nSpinner={models[model]}_spinner.gen"
                    f"\nGenString=chassis.gmt"
                    f"\nSounds={sounds[model]}.sfx"
                    f"\nUpgrades={models[model]}_upgrades.ini"
                    f"\nCameras=default_cams.cam"
                    f"\nHeadPhysics=headphysics.ini"
                    f"\nCockpit={models[model]}_cockpitinfo.ini"
                    f"\n\nNumber={num}"
                    f"\nTeam=\"{team_long}\""
                    f"\nPitGroup=\"Group12\""
                    f"\nDriver=\"{name}\""
                    f"\nDescription=\"#{num}\""
                    f"\nEngine=\"5.397cc V8 HEMI\""
                    f"\nManufacturer=\"Dodge\""
                    f"\nClasses=\"{clasS.upper()}{role.lower()}\""
                    f"\n\nFullTeamName=\"{team_long}\""
                )
                f.write("\nTeamFounded=2013\nTeamHeadquarters=\"Mula\"\nTeamStarts=1\nTeamPoles=0\nTeamWins=0\nTeamWorldChampionships=0")
                f.write(f"\nCategory=\"{clasS.upper()} {role.upper()}\"")
            else:
                f.write(
                    f"defaultLivery={team_short}_{num}.dds"
                    f"\nHDVehicle={team_short}.hdv"
                    f"\nGraphics={model}_Upgrades.gen"
                    f"\nSpinner={model}CE_spinner.gen"
                    f"\nUpgrades={model}_upgrades.ini"
                    f"\nGenString="
                    f"\nCameras={model}_cams.cam"
                    f"\nSounds={model}.sfx"
                    f"\nHeadPhysics=headphysics.ini"
                    f"\nCockpit={model}_cockpitinfo.ini"
                    f"\n\nNumber={num}"
                    f"\nTeam=\"{team_long}\""
                    f"\nPitGroup=\"Group12\""
                    f"\nDriver=\"{name}\""
                    f"\nDescription=\"#{num}\""
                    f"\nEngine=\"Prodrive\""
                    f"\nManufacturer=\"888 Race Engineering\""
                    f"\nClasses=\"{clasS.upper()}{role.lower()}\""
                    f"\n\nFullTeamName=\"{team_long}\""
                )
                f.write("\nTeamFounded=2013\nTeamHeadquarters=\"Mula\"\nTeamStarts=1\nTeamPoles=0\nTeamWins=0\nTeamWorldChampionships=0")
                f.write(f"\nCategory=\"{clasS.upper()} {role.upper()}\"")

if __name__ == "__main__":
    generate_veh()
