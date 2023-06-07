"""
5) Сгенерировать список используя генератор списков.
В списке должно быть 10 элементов в произвольном случайном диапазоне.
 Перевести все числа в строку и получить из списка -  строку.
"""
import random
a = random.randint(0, 1000)
list1 = [random.randint(0, a) for i in range(10)]
print(list1)
list2 = []
for i in list1:
    str1 = str(i)
    list2.append(i)
print(','.join(map(str,list2)))