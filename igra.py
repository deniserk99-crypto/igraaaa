import random

heroes = [
    {"name": "Орк Иван", "hp": 150, "damage": (15, 30)},
    {"name": "Эльф Наташа", "hp": 100, "damage": (10, 25)},
    {"name": "Человек Адам", "hp": 120, "damage": (12, 22)},
    {"name": "Гном Илья", "hp": 130, "damage": (8, 20)}
]

print("Битва")

for hero in heroes:
    print(hero["name"], "- HP:", hero["hp"])

print("\nБИТВА НАЧАЛАСЬ!\n")

while len(heroes) > 1:

    attacker = random.choice(heroes)
    target = random.choice([h for h in heroes if h != attacker])

    damage = random.randint(
        attacker["damage"][0],
        attacker["damage"][1]
    )

    target["hp"] -= damage

    print(
        attacker["name"], "атакует",
        target["name"], "и наносит", damage, "урона!"
    )

    if target["hp"] <= 0:
        print(target["name"], "погиб!")
        heroes.remove(target)
    else:
        print("У", target["name"], "осталось", target["hp"], "HP")

    print()

print("================================")
print("ПОБЕДИТЕЛЬ:", heroes[0]["name"])
print("Осталось HP:", heroes[0]["hp"])
print("================================")
