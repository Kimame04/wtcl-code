
if __name__ == "__main__":
    team = input("team: ")
    model = input("model: ").lower()
    if model == 'fg' or model == 've':
        aero, drag, weight = input("upgrades, separate commas: ").replace(" ", "").split(",")
        aero_value = 0.200 - 0.01 * int(aero)
        drag_value = 0.080 - 0.01 * int(drag)
        weight_value = 1050 - 10 * int(weight)
        with open(f'{team}.hdv', 'w') as f:
            with open('reference_hdv/VE.hdv') as ve: # works for FG also
                for line in ve:
                    f.write(line.replace("Mass=1440.0", f"Mass={weight_value}").replace("RWDragParams=(0.054, 0.0095, 0.0)", f"RWDragParams=({drag_value}, 0.0095, 0)").replace("BodyDragBase=(0.120)", f"BodyDragBase=({aero_value})"))
