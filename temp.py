import os

directory = f'{os.getcwd()}/wtcl'

for filename in os.listdir(directory):
    if ".veh" in filename: 
        with open(f"{directory}_copy/{filename}", 'w+') as f1:
            with open(f"{directory}/{filename}", 'r+') as f2:
                for line in f2:
                    if "Category=" in line:
                        cat = line.split("\"")[1]
            tokens = cat.split(" ")
            series = tokens[0].upper()
            contract = tokens[1].lower()
            with open(f"{directory}/{filename}", 'r+') as f3:
                for lin in f3:
                    if "Classes=" in lin:
                        f1.write(lin.replace(lin,f"Classes=\"{series}{contract}\""))
                    else: 
                        f1.write(lin)

