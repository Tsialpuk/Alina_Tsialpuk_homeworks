"""
4) Имеется файл file.txt с текстом на латинице.
Напишите программу, которая выводит следующую статистику по тексту:
•	количество букв латинского алфавита;
•	число слов;
•	число строк.
Пример ввода и вывода
Предположим, что file.txt содержит приведенный ниже текст:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

"""
with open('file.txt', 'r') as file:
    elements = file.readlines() #создаем список из файла
    print(elements)
stroki = 0
bykvu = 0
words = 0
for elem in elements:
    words += len(elem.split())
    bykvu += sum(map(str.isalpha, elem))
    stroki += 1
print(f' Количество букв латинского алфавита {bykvu},'
      f'Количество слов в тексте {words} '
      f'Количество строк в тексе: {stroki},')