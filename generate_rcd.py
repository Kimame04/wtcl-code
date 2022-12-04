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
                f"\nDateofBirth=2-28-85"
                f"\nStarts=28"
                f"\nPoles=2"
                f"\nWins=1"
                f"\nDriversChampionships=0"
                f"\nAggression={row['Aggression']}"
                f"\nReputation={row['Reputation']}"
                f"\nCourtesy={row['Composure']}"
                f"\nComposure={row['Composure']}"
                f"\nSpeed={row['Speed']}"
                f"\nCrash=6.82"
                f"\nRecovery=78.85"
                f"\nCompletedLaps=92.66"
                f"\nMinRacingSkill={row['Minimum Racing Skill']}\n}}"
            )
            