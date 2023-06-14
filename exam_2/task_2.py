"""
2)Найти в списке те элементы,
значение которых меньше среднего арифметического, взятого от всех элементов списка.
"""
list_1 = [1, 3, 4, 5, 6, 7, 8, 9, 2]
list_2 = []
print(f'Данный список: {list_1}')
sum = 0
for i in list_1:
    x = len(list_1)
    sum += i
srednee_arif = sum / x
print(f'Среднее арифметическое данного списка: {srednee_arif}')
for i in list_1:
    if i < srednee_arif:
        list_2.append(i)
print(f'Числа, которые меньше среднего арифметического: {list_2}')
