"""
8.Напишите программу, которая подключает модуль math и,
используя значение числа \pi  из этого модуля,
вводим радиус круга  и находим периметр этого круга, результат вывести на экран.
"""
from math import pi
radius = int(input('Введите радиус круга: '))
perimetr = 2 * pi * radius
print(f'Периметр круга равен: {perimetr}')