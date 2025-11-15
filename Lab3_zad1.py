paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"czas: {czas}s - pozostałe paliwo: {paliwo}l")
    paliwo -= paliwo_zuzyte_na_s
    czas += 1
print("Koniec lotu")