"""
есть список с четными и нечетными элементами. Посчитать количество четных и нечетных элементов
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
chet_num = 0
nechet_num = 0
for i in list1:
    if i % 2 == 0:
        chet_num += 1
    else:
        nechet_num += 1
print(f"Количество четных элементов: {chet_num}")
print(f"Количество нечетных элементов: {nechet_num}")