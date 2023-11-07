from math import *
import itertools


message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'

def  CalculateSquareRoot (Number: float) -> float:
    """ Вычисляет квадратный корень"""
    return  sqrt(Number )

def calc(your_number: float) -> str :
    if your_number <= 0:
        return ''
    root = 0
    return f"Мы вычислили квадратный корень из введённого вами числа. Это будет: {CalculateSquareRoot(your_number)}"


print(message)
print(calc (25.5))