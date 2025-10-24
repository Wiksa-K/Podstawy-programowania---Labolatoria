# Pobieranie wartości "a" i "b" od użytkownika i zamiana ich na liczby zmiennoprzecinkowe
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
# Sprawdzenie czy użytkownik nie dzieli przez 0
if b == 0:
    print("Nie można dzielić przez 0")
# Jeśli b nie jest zerem - zostają wykonane wszystkie działania matematyczne
else:
    dodawanie = a + b
    odejmowanie = a - b
    mnozenie = a * b
    dzielenie = a / b
    dzielenie_calkowite = a // b
    potegowanie = a ** b
    # Wypisanie wyników działań
    print()
    print("Dodawanie:", dodawanie)
    print("Odejmowanie: ", odejmowanie)
    print("Mnożenie:", mnozenie)
    print("Dzielenie z resztą:", dzielenie)
    print("Dzielenie całkowite:", dzielenie_calkowite)
    print("Potęgowanie:", potegowanie)
