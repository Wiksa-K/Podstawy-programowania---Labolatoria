wynik = int(input("Podaj zdobytą liczbę punktów: "))

if wynik > 80:
    print("Zaliczyłeś egzamin")
elif wynik <= 80 and wynik >= 50 :
    print("Możesz poprawić egzamin")
elif wynik < 50:
    print("Musisz poprawić egzamin")