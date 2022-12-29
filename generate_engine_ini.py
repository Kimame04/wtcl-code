import click

@click.command()
@click.option('--team', help='team shorthand')
@click.option('--series', help='series (e.g ITCL, WTCL)')
@click.option('--ce', help='chief engineer effect')
@click.option('--num_upgrades', help='reliability level')

def generate_engine_ini(team, series, ce, num_upgrades):
    ce_multiplier = 1 + ce * 0.01
    if num_upgrades >= 0:
        true_reliability = 37000 + 500 * num_upgrades * ce_multiplier
    else: 
        true_reliability = 37e3 + 500 * num_upgrades
    with open(f"{series}/{team}.ini", 'w') as f:
        engine_filenames = {'itcl': 'gt_engine', 'wtcl': 'V8SC_E85_Engine'}
        with open(f'reference_engine_ini/{engine_filenames[series]}.ini') as ref_file:
            for line in ref_file:
                f.write(line.replace("LifetimeAvg=72000", f"LifetimeAvg={true_reliability}").replace("LifetimeAvg=54000", f"LifetimeAvg={true_reliability}"))


if __name__ == "__main__":
    generate_engine_ini()
