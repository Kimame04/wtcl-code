def generate_engine_ini(team, clasS, ce_multiplier, num_upgrades):
    if num_upgrades >= 0:
        true_reliability = 37000 + 500 * num_upgrades * ce_multiplier
    else: 
        true_reliability = 37e3 + 500 * num_upgrades
    with open(f"{clasS}/{team}.ini", 'w') as f:
        engine_filenames = {'itcl': 'gt_engine', 'wtcl': 'V8SC_E85_Engine'}
        with open(f'reference_engine_ini/{engine_filenames[clasS]}.ini') as ref_file:
            for line in ref_file:
                f.write(line.replace("LifetimeAvg=72000", f"LifetimeAvg={true_reliability}").replace("LifetimeAvg=54000", f"LifetimeAvg={true_reliability}"))


if __name__ == "__main__":
    team = input("team: ")
    clasS = input("class: ").lower()
    ce_multiplier = 1 + float(input("chief engineer effect (in %): ")) * 0.01
    num_upgrades = int(input("reliability upgrades: "))
    generate_engine_ini(team, clasS, ce_multiplier, num_upgrades)
