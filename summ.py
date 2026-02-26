
# ✅ Было

def add_numbers(x, y):
    return x + y



from math import *
import itertools



def  CalculateSquareRoot (Number ):
    return  sqrt(Number )

def calc(your_number) :
    if your_number<=0:
        return    
     
    root = 0
    return f"Мы вычислили квадратный корень из введённого вами числа. Это будет: {CalculateSquareRoot(your_number)}"



x = 10
y = 5

print('Сумма чисел: ', add_numbers(x, y))

print(calc (25.5))


# ✅ Так должно быть.


from math import sqrt
from typing import Optional


def add_numbers(first: int, second: int) -> int:
    """Возвращает сумму двух целых чисел."""
    return first + second


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень числа."""
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    """Возвращает строку с результатом или None, если число ≤ 0."""
    if your_number <= 0:
        return None

    # ✅ Вызов функции и присваивание результата переменной
    root = calculate_square_root(your_number)

    return (
        'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {root}'
    )


first_number: int = 10
second_number: int = 5