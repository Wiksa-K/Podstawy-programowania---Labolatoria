def sum_digits(n: int) -> int:
    """
    Oblicza sumę cyfr liczby w sposób rekurencyjny,

    Args:
        n: liczba całkowita nieujemna

    Returns:
        Suma cyfr liczby n
    """

    if n < 10:
        return n
    return n % 10 + sum_digits(n//10)
print(sum_digits(5))