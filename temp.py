import os

directory = f'{os.getcwd()}/wtcl'

for filename in os.listdir(directory):
    if ".veh" in filename: 
        with open(f"{directory}_copy/{filename}", 'w+') as f1:
            with open(f"{directory}/{filename}", 'r+') as f3:
                for lin in f3:
                    if "Upgrades= " in lin:
                        tokens = lin.split(" ")
                        f1.write(lin.replace(lin,f"Upgrades={tokens[1]}"))
                    elif "HDVehicle= " in lin:
                        tokens = lin.split(" ")
                        f1.write(lin.replace(lin,f"HDVehicle={tokens[1]}"))
                    else: 
                        f1.write(lin)

