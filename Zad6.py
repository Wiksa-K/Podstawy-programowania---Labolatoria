droga = float(input("Podaj pokonany dystans: ")) # Funkcja "float()" pozwala operować na podanych liczbach (dodawanie/mnożenie/dzielenie) oraz sprawia, że będą zmiennoprzecinkowe, a "input()" pozwoli wprowadzić dane do zmiennej
srednie_spalanie = float(input("Podaj średnie spalanie samochodu (w litrach na 100km): ")) # Funkcja "float()" pozwala operować na podanych liczbach (dodawanie/mnożenie/dzielenie) oraz sprawia, że będą zmiennoprzecinkowe, a "input()" pozwoli wprowadzić dane do zmiennej
cena_paliwa = 6.5 # Cena paliwa za litr
zuzycie = (srednie_spalanie / 100) * droga # Obliczanie zużycia paliwa
koszt_podrozy = zuzycie * cena_paliwa # Obliczenie kosztu podróży

print("Przewidywane zużycie paliwa wynosi:",zuzycie, "litrów","\nSzacunkowy koszt podróży wynosi:",koszt_podrozy, "zł") # Wypisanie wyników z użyciem zmiennych