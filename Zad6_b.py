import random # Importowanie biblioteki "math" w celu użycia funkcji random.randint()

droga = random.randint(1, 10000) # Używamy funkcji random.randint() aby wylosować liczbę spośród podanego zakresu
srednie_spalanie = float(input("Podaj średnie spalanie samochodu (l/100km): ")) # Funkcja "float()" pozwala operować na podanych liczbach (dodawanie/mnożenie/dzielenie) oraz sprawia, że będą zmiennoprzecinkowe, a funkcja "input()" pozwoli wprowadzić dane do zmiennej
cena_paliwa = float(input("Podaj cenę paliwa (zł/l): ")) # Funkcja "input()" pozwoli użytkownikowi wprowadzić cenę paliwa do zmiennej
zuzycie = round(srednie_spalanie / 100 * droga, 2) # Obliczanie zużycia paliwa, funkcja "round()" zaokrągli wynik do 2 miejsc po przecinku
koszt_podrozy = round(zuzycie * cena_paliwa, 2) # Obliczenie kosztu podróży, funkcja "round()" zaokrągli wynik do 2 miejsc po przecinku

print(f'Przewidywane zużycie paliwa wynosi: {zuzycie} litrów, a szacunkowy koszt podróży wynosi: {koszt_podrozy} zł') # Wypisanie wyniku z użyciem zmiennych oraz użycie funkcji "f''" która pozwali na użycie zmiennych w łatwiejszy sposób