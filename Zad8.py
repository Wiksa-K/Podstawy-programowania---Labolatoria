from math import sqrt # Importujemy funkcje "sqrt" (pierwiastek kwadratowy) z modułu "math"
# Pobranie współczynników równania kwadratowego od użytkownika
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

# Sprawdzenie czy a = 0 (bo wtedy równanie nie jest kwadratowe)
if a == 0:
    print("a nie może być równe 0")
else:
    delta = (b ** 2) - (4 * a * c) # Obliczanie delty
    # Jeśli delta = 0 - równanie ma jedno rozwiązanie
    if delta == 0:
        x_zero = (b * -1) / (2 * a)
        print(f"X0 = {x_zero}")
    else:
        # Jeśli delta > 0 - równanie ma dwa rozwiązania
        if delta > 0:
            pierwiastek_z_delty = sqrt(delta)
            x_jeden = round(((b * -1) + pierwiastek_z_delty) / (2 * a),2) # Obliczanie pierwszego pierwiastka równiania
            x_dwa = round(((b * -1) - pierwiastek_z_delty) / (2 * a),2) # Obliczanie drugiego pierwiastka równania
            print(f"x1 = {x_jeden} x2 = {x_dwa}") # Wypisanie wyników
        # Jeśli delta < 0 - brak rozwiązań
        else:
            print("Równanie sprzeczne")
