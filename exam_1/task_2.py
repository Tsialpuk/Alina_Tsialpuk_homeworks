"""
2.	Написать программу для вычисления значения выражений.
Проверить правильность выполнения задания с помощью тестовых значений.
"""
import math
a = int(input('Введите значение переменной: а = '))
b = int(input('Введите значение переменной: b = '))
y = int(input('Введите значение переменной: y = '))
y1 = (1/4) * (math.sin(a + b - y) + math.sin(b + y - a) + math.sin(y + a - b) - math.sin(a + b + y))

print(f'y1 = {y1}')
