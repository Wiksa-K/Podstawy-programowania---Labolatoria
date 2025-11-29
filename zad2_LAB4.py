imiona = ["Wiktoria", "Zuzanna", "Aurelia", "Marta"]
print(imiona)

#a
imiona.sort()
print(imiona)

#b
imiona.extend(["Ania", "Paulina"])
print(imiona)
ost = imiona.pop()
print(ost, imiona)

#c
imiona.insert(2, "Kasia")
print(imiona)

#d
imiona.reverse()
imiona = imiona + imiona
print(imiona)