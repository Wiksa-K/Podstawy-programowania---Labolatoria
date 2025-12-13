def swap(lst, i , j):
    if not isinstance(lst, list):
        raise TypeError("Pierwszy argument musi być literą")
    if not isinstance(i, int) or not isinstance(j, int):
        raise TypeError("Indeksy muszą być liczbami całkowitymi")
    if len(lst) == 0:
        raise ValueError("Lista jest pusta")

    try:
        lst[i], lst[j] = lst[j], lst[i]
    except IndexError:
        raise IndexError("Indeks poza zakresem listy")
