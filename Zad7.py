# Pobieranie wartości "a" i "b" od użytkownika i zamiana ich na liczby zmiennoprzecinkowe
a = float(input("Podaj liczbe a: "))
b = float(input("Podaj liczbe b: "))

# Sprawdzanie, czy współczynnik "a" jest równy zero
if a == 0:
    # Jeśli a = 0 i b = 0 - równanie jest tożsamościowe (ma nieskończenie wiele rozwiązań)
    if b == 0:
        print("Równanie tożsamościowe")
    # Jeśli a = 0, ale b nie jest równe 0 - równanie jest sprzeczne (nie ma rozwiązań)
    else:
        print("Równanie sprzeczne")
# W przeciwnym wypadku (a nie jest równe 0) - można obliczyć rozwiązanie równania
else:
    x = (b * -1)/a # Oblicznie wartości "x" z równania 
    print(x) # Wypisanie wyniku