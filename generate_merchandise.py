import random

def generate_merchandise(base, rep, series):
    multipliers = {'itcl': 3, 'wtcl': 5}
    dice_roll = random.randint(30, 50) + random.randint(30, 50) + random.randint(30, 50) + random.randint(30, 50)
    new_base = base + rep * dice_roll * multipliers[series]
    print(f"new fanbase: {new_base} (change: {new_base - base})")

if __name__ == '__main__':
    base = int(input("enter base fanbase: "))
    rep = int(input("enter reputation: "))
    series = input("enter series: ").lower()
    generate_merchandise(base, rep, series)

