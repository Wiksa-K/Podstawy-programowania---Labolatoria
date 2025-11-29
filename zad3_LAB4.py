imie = input("Podaj imię: ")
print("Witaj", imie)

wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)

nazwisko = input("Podaj nazwisko: ")
inicjaly = imie[0].upper() + "." + nazwisko[0].upper()
print(inicjaly)

print(nazwisko * 5)

razem = imie + nazwisko
print(razem)

imie_p = len(imie) // 2
nazwisko_p = len(nazwisko) // 2
pol = imie[:imie_p] + nazwisko[nazwisko_p:]
print(pol)