import random
from countries import getCountries

genders = ['M', 'F']
countries = getCountries()
age_cats = ['youth', 'standard']

def add_variance(stat):
    return stat + random.randint(-10, 10)

def add_youth_variance(stat, age):
    return stat + random.randint(0, 5) * (age - 14)

if __name__ == "__main__":
    gender = random.choice(genders)
    country = random.choice(countries)
    age_cat = random.choice(age_cats)
    if age_cat == 'standard': 
        base = 50 + random.randint(0, 40)
        age = random.randint(24, 40)
        stat_block = [base, base, base, base]
        output = list(map(add_variance, stat_block))

    else: 
        base = 30 + random.randint(0, 10)
        age = random.randint(15, 23)
        stat_block = [base, base, base, base]
        output = list(map(add_youth_variance, stat_block, [age, age, age, age]))

    output.insert(0, round(sum(output)/len(output)))
    rep = 0
    for i in range(5):
        rep += random.randint(4, 18)
    output.insert(len(output), rep)

    print(f"{country} {gender} {age} {output}")