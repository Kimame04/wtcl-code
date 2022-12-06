import pandas as pd
import unicodedata

if __name__ == '__main__':
    dest = "drivers/"
    df = pd.read_excel('drivers.xlsx')
    for index, row in df.iterrows():
        formatted_name = unicodedata.normalize('NFD', row['Name']).encode('ascii', 'ignore').decode()
        filename = formatted_name.replace(" ", "") + ".rcd"
        with open(f"{dest}{filename}", "w") as f:
            f.write(
                f"{formatted_name}\n{{"
                f"\nNationality=Danish"
                f"\nDateofBirth=1-1-11"
                f"\nStarts=0"
                f"\nPoles=0"
                f"\nWins=0"
                f"\nDriversChampionships=0"
                f"\nAggression={row['Aggression']}"
                f"\nReputation={row['Reputation']}"
                f"\nCourtesy={row['Composure']}"
                f"\nComposure={row['Composure']}"
                f"\nSpeed={row['Speed']}"
                f"\nCrash=0"
                f"\nRecovery=0"
                f"\nCompletedLaps=0"
                f"\nMinRacingSkill={row['Minimum Racing Skill']}\n}}"
            )
            