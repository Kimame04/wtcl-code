import generate_engine_ini, generate_hdv, generate_veh

if __name__ == "__main__":
    team_short = input("team code: ")
    team_long = input("team name: ")
    model = input("model code: ")
    clasS = input("class: ") # itcl, wtcl
    pair_1 = input('Enter driver 1 name, number, contract: ').split(',')
    pair_2 = input('Enter driver 2 name, number, contract: ').split(',')
    pair_3 = input('Enter driver 3 name, number, contract: ').split(',')
    ce_multiplier = 1 + float(input("chief engineer effect (in %): ")) * 0.01
    pairs = [pair_1, pair_2, pair_3]
    
    generate_hdv.generate_hdv(team_short, model, ce_multiplier)
    generate_engine_ini.generate_engine_ini(team_short, clasS, ce_multiplier)
    generate_veh.generate_veh(team_short, team_long, model, pairs, clasS)
