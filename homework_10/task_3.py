"""
Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(f'Первый список а: {a}')
print(f'Второй список b: {b}')
set_a = set(a) #перевод списка во множество
set_b = set(b) #перевод списка во множество
c = set_a.intersection(set_b) #проверяем на пересечения
list_c = list(c) #переводим множество в список
print(f'Cписок, который состоит из элементов, общих для этих двух списков: {list_c}')


