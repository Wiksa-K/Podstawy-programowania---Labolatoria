def stworz_profil(name: str, email:str, **kwargs):
    if not isinstance(name, str) or not isinstance(email, str):
        raise TypeError("Imię i email muszą być stringami")

    profil = {
        "name": name.strip(),
        "email": email.strip(),
    }

    if len(kwargs) < 3:
        raise ValueError("Podaj minimum 3 dodatkowe informacje")

    for key, value in kwargs.items():
        profil[key] = value

    return profil

print(stworz_profil("Wiksa", "wika@ok.pl", age=19, miasto="Rzeszów", kolor="różowy"))
