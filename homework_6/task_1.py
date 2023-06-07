"""
дан список. list = [15,48, 'hello',6,19,'world'].
все числа этого списка проверить на четность. Если число четное, то посчитать сумму его цифр
Если нечетное, то заменить его на 1 в списке. Все слова: посчитать количество гласных и согласных
вывести все на экран
"""
list1 = [15, 48, 'hello', 6, 19, 'world']
print(list1)
list2 = []
for i in list1:
    if type(i) == int:
        if i % 2 == 0:
            num1 = i % 10
            num2 = i // 10
            num3 = num1 + num2
            list2.append(num3)
        else:
            ind = list1.index(i)
            list1[ind] = 1
print(f'{list2}: список с суммой чётных чисел')
print(f'{list1}: список с заменой  нечётный чисел на 1')

list3 = [i for i in list1 if type(i) == str]
str1 = ''.join(list3)
glass = 0
soglass = 0
for i in str1:
    if i == 'a':
        glass += 1
    elif i == 'o':
        glass += 1
    elif i == 'e':
        glass += 1
    elif i == 'i':
        glass += 1
    elif i == 'u':
        glass += 1
    elif i == 'y':
        glass += 1
    else:
        soglass += 1

print(f'количество гласных букв в {list1}: {glass} ')
print(f'количество согласных букв в {list1}: {soglass}')
