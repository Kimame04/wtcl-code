def generate_engine_ini(team, series, ce, num_upgrades):
    ce_multiplier = 1 + ce * 0.01
    if num_upgrades >= 0:
        true_reliability = 18e3 + 500 * num_upgrades * ce_multiplier
    else: 
        true_reliability = 18e3 + 500 * num_upgrades
    with open(f"{series}/{team}.ini", 'w') as f:
        engine_filenames = {'itcl': 'gt_engine', 'wtcl': 'V8SC_E85_Engine'}
        with open(f'reference_engine_ini/{engine_filenames[series]}.ini') as ref_file:
            for line in ref_file:
                f.write(line.replace("LifetimeAvg=72000", f"LifetimeAvg={true_reliability}").replace("LifetimeAvg=54000", f"LifetimeAvg={true_reliability}").replace("LifetimeVar=5000", "LifetimeVar=6000").replace("LifetimeVar=7200", "LifetimeVar=6000"))
