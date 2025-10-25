#a
gol = int(input("Podaj liczbę zdobytych bramek: "))

bonus = gol * 10

if gol > 5 and gol < 10:
    bonus = bonus + 5
if gol > 10:
    bonus = bonus + 10

print(bonus)


#b
gol = int(input("Podaj liczbę zdobytych bramek: "))

bonus = gol * 10

if gol > 5 and gol < 10:
    bonus = bonus + 5
if gol > 5 and gol > 10:
    bonus = bonus + 15

print(bonus)
