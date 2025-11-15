licznik = 0
liczba = 2
liczby_pierwsze = []

while licznik < 10:
    for i in range(2, liczba):
        if liczba % i == 0:
            break
    else:
        liczby_pierwsze.append(str(liczba))
        licznik += 1
    liczba += 1

print(",".join(liczby_pierwsze))
