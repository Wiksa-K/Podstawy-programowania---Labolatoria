stopnie = (
    "Szeregowy",
    "Kapral",
    "Śerżant",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)

ilosc_stopni = len(stopnie)
Major_index = stopnie.index("Major") if "Major" in stopnie else None
Pulkownik_wystepowanie = "Pułkownik" in stopnie

print(ilosc_stopni)
print(Major_index)
print(Pulkownik_wystepowanie)