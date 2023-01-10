
def generate_hdv(team, model, ce, aero, drag, weight):
    bop = {'fg': 5, 've': 0, 'chr': 15, 'css': 0, 'egl': 0, 'mts': 0, 'rnl': 0}
    ce_multiplier = 1 + ce * 0.01
    if model == 'fg' or model == 've': #V8Factor
        aero_value = 0.200 - 0.01 * aero * ce_multiplier
        drag_value = 0.080 - 0.01 * drag * ce_multiplier
        weight_value = 1050 - 10 * weight * ce_multiplier + bop[model]
        with open(f'wtcl/{team}.hdv', 'w') as f:
            with open(f'reference_hdv/{model.upper()}.hdv') as ve:
                for line in ve:
                    f.write(line.replace("Mass=1440.0", f"Mass={weight_value}").replace("RWDragParams=(0.054, 0.0095, 0.0)", f"RWDragParams=({drag_value}, 0.0095, 0)").replace("BodyDragBase=(0.120)", f"BodyDragBase=({aero_value})"))
    else: #ITCC 2013
        aero_value = 0.300 - 0.01 * aero * ce_multiplier
        weight_value = 1100 - 10 * weight * ce_multiplier + bop[model]
        with open(f'itcl/{team}.hdv', 'w') as f:
            with open(f'reference_hdv/{model.upper()}.hdv') as itcl:
                for line in itcl:
                    f.write(line.replace("Mass=906.0", f"Mass={weight_value}").replace("BodyDragBase=(0.302)", f"BodyDragBase=({aero_value})").replace("RWDragParams=(0.025, 0.025, 0)", "RWDragParams=(0.100, 0.025, 0)"))
