
bop = {'fg': 0, 've': 0, 'chr': 10, 'css': 0, 'egl': 0, 'mts': 5, 'rnl': 0}

if __name__ == "__main__":
    team = input("team: ")
    model = input("model code: ").lower()
    if model == 'fg' or model == 've': #V8Factor
        aero, drag, weight = input("upgrades, separate commas: ").replace(" ", "").split(",")
        aero_value = 0.200 - 0.01 * int(aero)
        drag_value = 0.080 - 0.01 * int(drag)
        weight_value = 1050 - 10 * int(weight) + bop[model]
        with open(f'wtcl/{team}.hdv', 'w') as f:
            with open(f'reference_hdv/{model.upper()}.hdv') as ve:
                for line in ve:
                    f.write(line.replace("Mass=1440.0", f"Mass={weight_value}").replace("RWDragParams=(0.054, 0.0095, 0.0)", f"RWDragParams=({drag_value}, 0.0095, 0)").replace("BodyDragBase=(0.120)", f"BodyDragBase=({aero_value})"))
    else: #ITCC 2013
        aero, weight = input("upgrades, separate commas: ").replace(" ", "").split(",")
        aero_value = 0.300 - 0.01 * int(aero)
        weight_value = 1100 - 10 * int(weight) + bop[model]
        with open(f'itcl/{team}.hdv', 'w') as f:
            with open(f'reference_hdv/{model.upper()}.hdv') as itcl:
                for line in itcl:
                    f.write(line.replace("Mass=906.0", f"Mass={weight_value}").replace("BodyDragBase=(0.302)", f"BodyDragBase=({aero_value})").replace("RWDragParams=(0.025, 0.025, 0)", "RWDragParams=(0.100, 0.025, 0)"))
