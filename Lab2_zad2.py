x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))
z = int(input("Podaj trzecią liczbę: "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print(x, y, z)