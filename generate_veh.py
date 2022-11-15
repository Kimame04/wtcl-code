sounds = {'chr': 'sonidos', 'css': 'sonidos', 'egl': 'sonidos3', 'mts': 'sonidos3', 'rnl': 'sonidos4'}
model_codes = {'chrysler': 'chr', 'bentley': 'css', 'eagle': 'egl', 'mitsubishi': 'mts', 'renault': 'rnl'}

if __name__ == "__main__":
    team_short = input('Enter short team name: ')
    team_long = input('Enter long team name: ')
    model = input('Enter model: ').lower()
    model_code = model_codes[model]
    pair_1 = input('Enter driver 1 name, number 1: ').split(',')
    pair_2 = input('Enter driver 2 name, number 2: ').split(',')
    pair_3 = input('Enter driver 3 name, number 3: ').split(',')
    pairs = [pair_1, pair_2, pair_3]
    classes = input('Enter class: ')
    for pair in pairs:
        with open(f"itcl/{team_short}_{pair[1]}.veh", 'w') as f:
            f.write(
                f"defaultLivery={team_short}_{pair[1]}.dds"
                f"\nHDVehicle={model}_hdv.hdv"
                f"\nGraphics={model}_gen.gen"
                f"\nSpinner={model}_spinner.gen"
                f"\nGenString=chassis.gmt"
                f"\nSounds={sounds[model_codes[model]]}.sfx"
                f"\nUpgrades={model}_upgrades.ini"
                f"\nCameras=default_cams.cam"
                f"\nHeadPhysics=headphysics.ini"
                f"\nCockpit={model}_cockpitinfo.ini"
                f"\n\nNumber={pair[1]}"
                f"\nTeam=\"{team_long}\""
                f"\nPitGroup=\"Group12\""
                f"\nDriver=\"{pair[0]}\""
                f"\nDescription=\"#{pair[1]}\""
                f"\nEngine=\"5.397cc V8 HEMI\""
                f"\nManufacturer=\"Dodge\""
                f"\nClasses=\"{classes}\""
                f"\n\nFullTeamName=\"{team_long}\""
            )
            f.write("\nTeamFounded=2013\nTeamHeadquarters=\"Mula\"\nTeamStarts=1\nTeamPoles=0\nTeamWins=0\nTeamWorldChampionships=0")
            f.write(f"\nCategory=\"{model.capitalize()}\"")