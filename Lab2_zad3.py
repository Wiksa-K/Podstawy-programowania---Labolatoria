Nazwa_pliku = str(input("Podaj pełną nazwę pliku: "))

wynik = Nazwa_pliku.endswith(".xlsx")

if wynik == True:
    print("Tak")
elif wynik == False:
    print("Nie")