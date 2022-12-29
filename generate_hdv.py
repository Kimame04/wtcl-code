

def generate_hdv(team, model, ce_multiplier, aero, drag, weight):
    bop = {'fg': 0, 've': 0, 'chr': 10, 'css': 0, 'egl': 0, 'mts': 5, 'rnl': 0, 'fg': 0, 've': 0}

    if model == 'fg' or model == 've': #V8Factor
        aero_value = 0.200 - 0.01 * int(aero) * ce_multiplier
        drag_value = 0.080 - 0.01 * int(drag) * ce_multiplier
        weight_value = 1050 - 10 * int(weight) * ce_multiplier + bop[model]
        with open(f'wtcl/{team}.hdv', 'w') as f:
            with open(f'reference_hdv/{model.upper()}.hdv') as ve:
                for line in ve:
                    f.write(line.replace("Mass=1440.0", f"Mass={weight_value}").replace("RWDragParams=(0.054, 0.0095, 0.0)", f"RWDragParams=({drag_value}, 0.0095, 0)").replace("BodyDragBase=(0.120)", f"BodyDragBase=({aero_value})"))
    else: #ITCC 2013
        aero_value = 0.300 - 0.01 * int(aero) * ce_multiplier
        weight_value = 1100 - 10 * int(weight) * ce_multiplier + bop[model]
        with open(f'itcl/{team}.hdv', 'w') as f:
            with open(f'reference_hdv/{model.upper()}.hdv') as itcl:
                for line in itcl:
                    f.write(line.replace("Mass=906.0", f"Mass={weight_value}").replace("BodyDragBase=(0.302)", f"BodyDragBase=({aero_value})").replace("RWDragParams=(0.025, 0.025, 0)", "RWDragParams=(0.100, 0.025, 0)"))


if __name__ == "__main__":
    team = input("team: ")
    model = input("model code: ").lower()
    ce_multiplier = 1 + float(input("chief engineer effect (in %): ")) * 0.01
    generate_hdv(team, model, ce_multiplier)
