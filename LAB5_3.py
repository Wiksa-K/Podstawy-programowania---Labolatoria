def liczy_parzyste(*liczby):
    return list(filter(lambda x: x%2 == 0, liczby))
print(liczy_parzyste(1, 2, 3, 4, 5, 6))