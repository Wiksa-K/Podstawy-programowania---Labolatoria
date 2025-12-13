import math

def funkcja_kwadratowa(a: float, b: float, c: float):
    """Oblicza pierwiastki funkcji kwadratowej

    Args:
        a: współczynnik przy x^2 (nie może być 0)
        b: współczynnik przy x
        c: wyraz wolny

    Returns:
        Brak pierwiastków, jeden pierwiastek

    Raises:
        ValueError: gdy a == 0
    """
    if a == 0:
        raise ValueError("To nie jest funkcja kwadratowa")

    delta = b**2 - 4*a*c

    if delta < 0:
        return "Brak pierwiastków rzeczywistych"
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return x1, x2

print(funkcja_kwadratowa(1, -3, 2))
