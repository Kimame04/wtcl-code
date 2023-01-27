import click
import pandas as pd

@click.command()
@click.option("--season", help="[season number] e.g s6")

def generate_jtcl_veh(season):
    excel_file = pd.ExcelFile('hub-cheatsheet.xlsx')
    df = excel_file.parse(f'jtcl-{season}')
    for index, row in df.iterrows():
        num = int(row['num'])
        with open(f"jtcl/clio-{num}.veh", 'w') as f:
            with open("reference_veh/ClioV6Cup_01.veh") as rep_file:
                for line in rep_file:
                    f.write(line.replace("Driver=\"Stig\"", f"Driver=\"{row['name']}\"").replace("Description=\"V6 Cup Blue\"", f"Description=\"#{num}\""))
    pass

if __name__ == "__main__":
    generate_jtcl_veh()