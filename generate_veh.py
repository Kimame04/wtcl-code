
def generate_veh(team_short, team_long, model, pairs, clasS):
    sounds = {'chr': 'sonidos', 'css': 'sonidos', 'egl': 'sonidos3', 'mts': 'sonidos3', 'rnl': 'sonidos4', 'fg': 'FG', 've': 'VE'}
    models = {'chr': 'chrysler', 'css': 'bentley', 'egl': 'eagle', 'mts': 'mitsubishi', 'rnl': 'renault', 'fg': 'Ford FG', 've': 'Holden VE'}

    for pair in pairs:
        with open(f"{clasS}/{team_short}_{pair[1]}.veh", 'w') as f:
            if clasS == 'itcl':
                f.write(
                    f"defaultLivery={team_short}_{pair[1]}.dds"
                    f"\nHDVehicle={team_short}.hdv"
                    f"\nGraphics={models[model]}_gen.gen"
                    f"\nSpinner={models[model]}_spinner.gen"
                    f"\nGenString=chassis.gmt"
                    f"\nSounds={sounds[model]}.sfx"
                    f"\nUpgrades={models[model]}_upgrades.ini"
                    f"\nCameras=default_cams.cam"
                    f"\nHeadPhysics=headphysics.ini"
                    f"\nCockpit={models[model]}_cockpitinfo.ini"
                    f"\n\nNumber={pair[1]}"
                    f"\nTeam=\"{team_long}\""
                    f"\nPitGroup=\"Group12\""
                    f"\nDriver=\"{pair[0]}\""
                    f"\nDescription=\"#{pair[1]}\""
                    f"\nEngine=\"5.397cc V8 HEMI\""
                    f"\nManufacturer=\"Dodge\""
                    f"\nClasses=\"ITCC\""
                    f"\n\nFullTeamName=\"{team_long}\""
                )
                f.write("\nTeamFounded=2013\nTeamHeadquarters=\"Mula\"\nTeamStarts=1\nTeamPoles=0\nTeamWins=0\nTeamWorldChampionships=0")
                f.write(f"\nCategory=\"{clasS.upper()} {pair[2].upper()}\"")
            else:
                f.write(
                    f"defaultLivery={team_short}_{pair[1]}.dds"
                    f"\nHDVehicle={model}.hdv"
                    f"\nGraphics={model}_Upgrades.gen"
                    f"\nSpinner={model}CE_spinner.gen"
                    f"\nUpgrades={model}_upgrades.ini"
                    f"\nGenString="
                    f"\nCameras={model}_cams.cam"
                    f"\nSounds={model}.sfx"
                    f"\nHeadPhysics=headphysics.ini"
                    f"\nCockpit={model}_cockpitinfo.ini"
                    f"\n\nNumber={pair[1]}"
                    f"\nTeam=\"{team_long}\""
                    f"\nPitGroup=\"Group12\""
                    f"\nDriver=\"{pair[0]}\""
                    f"\nDescription=\"#{pair[1]}\""
                    f"\nEngine=\"Prodrive\""
                    f"\nManufacturer=\"888 Race Engineering\""
                    f"\nClasses=\"V8SCCE\""
                    f"\n\nFullTeamName=\"{team_long}\""
                )
                f.write("\nTeamFounded=2013\nTeamHeadquarters=\"Mula\"\nTeamStarts=1\nTeamPoles=0\nTeamWins=0\nTeamWorldChampionships=0")
                f.write(f"\nCategory=\"{clasS.upper()} {pair[2].upper()}\"")

if __name__ == "__main__":
    team_short = input('Enter short team name: ')
    team_long = input('Enter long team name: ')
    model = input('Enter model: ').lower()
    pair_1 = input('Enter driver 1 name, number, series: ').split(',')
    pair_2 = input('Enter driver 2 name, number, series: ').split(',')
    pair_3 = input('Enter driver 3 name, number, series: ').split(',')
    pairs = [pair_1, pair_2, pair_3]
    generate_veh(team_short, team_long, model, pairs)
