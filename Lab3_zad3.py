ulice = [ "Jagodowa" , "Lipowa" , "Kwiatowa" , "Kasztanowa" , "Polna"]

bloki = [1,2,3,4,5]
mieszkania = ["/1","/2","/3","/4","/5","/6","/7", "/8", "/9","/10"]

for ulica in ulice:
    for blok in bloki:
        for mieszkanie in mieszkania:
            print(f"Ulica: {ulica} {blok}{mieszkanie}")