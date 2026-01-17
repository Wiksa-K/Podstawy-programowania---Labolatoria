import pandas as pd
data = pd.read_csv("dane.csv", sep=";")
df = pd.DataFrame(data)

df["Marża"] = (df["Sprzedaż"] - df["Koszt"]) / df["Sprzedaż"]

wynik = df.loc[
    (df["Kraj"] == "DE") & (df["Rok"] >= 2023),
    ["Sprzedaż" , "Marża"]
]

print(wynik)