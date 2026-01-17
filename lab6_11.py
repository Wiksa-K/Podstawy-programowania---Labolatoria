import pandas as pd

data = pd.read_csv("dane.csv", sep=";")
print(data.head())

df = pd.DataFrame(data)

df["Marża"] = (df["Sprzedaż"] - df["Koszt"]) / df["Sprzedaż"]

df = df.sort_values(by = ["Rok", "Kraj"], ascending = True)
print(df)