"""
4) Дано три числа. Найти количество положительных чисел среди них
"""
num_1 = int(input('введите первое число:'))
num_2 = int(input('введите второе число:'))
num_3 = int(input('введите третье число:'))
list1 = [num_1, num_2, num_3]
koll_polog = 0
for i in list1:
    if i > 0:
        koll_polog += 1
print(f'Количество положительных чисел: {koll_polog}')
