import unicodedata
import click
import pandas as pd

@click.command()
@click.option("--series", help="itcl or wtcl?")
@click.option("--filename", default="results.xlsx", help="name of excel file with quali order")
@click.option("--pname", help="name of player in rFactor (e.g alexis, proba123)")

def generate_gdb_section(filename, pname, series):
    excel_file = pd.ExcelFile(filename)
    df = excel_file.parse('Sheet1')
    quali_order = df.values.tolist()
    write_file(f"{series}-feature-race-grid", quali_order, pname)
    if series.lower() == 'wtcl':
        num = int(len(quali_order) / 2) + 1
        sprint_order = quali_order[:num][::-1] + quali_order[num:]
        write_file(f"{series}-sprint-race-grid", sprint_order, pname)

def write_file(filename, order, pname):
    with open(f"{filename}.txt", "w") as f:
        f.write(" // Add this in your track .gdb file.\n")
        f.write("Qualifying{\n")
        for driver in order:
            name = unicodedata.normalize('NFD', str(driver[0])).encode('ascii', 'ignore').decode()
            f.write(f"{name} = {50 + order.index(driver)}\n")
        f.write(f"{pname} = {51 + len(order)}\n")
        f.write("}\n\n")
        f.write("PitStopStrategies{\n")
        for driver in order:
            name = unicodedata.normalize('NFD', str(driver[0])).encode('ascii', 'ignore').decode()
            f.write(f"{name} = 1 - {50 + order.index(driver)}\n")
        f.write(f"{pname} = 1 - {51 + len(order)}\n")
        f.write("}\n\n")


if __name__ == "__main__":
    generate_gdb_section()
