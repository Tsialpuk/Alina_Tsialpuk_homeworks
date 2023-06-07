"""
1) При заданном целом числе n посчитайте n + nn + nnn.
"""
try:
    n = int(input('Введите целое число n:'))
    nn = n * 10 + n
    nnn = nn * 10 + n
    result = n + nn + nnn
except ValueError:
    print('данные введены некорректно')
else:
    print(f'результат n + nn + nnn: {result}')
finally:
    print('окончание программы')
