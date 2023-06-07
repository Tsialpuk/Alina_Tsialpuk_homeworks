"""
3)	В текстовом файле посчитать количество строк,
 а также для каждой отдельной строки определить количество в ней символов.
"""
with open('text_3.txt', 'r', encoding='utf8') as file:
    elements = file.readlines() #создаем список из файла
    print(elements)
stroki = 0
list1 = []
for i in elements:
    i = i[:-1] #убираем /n для подсчета строк
    stroki += 1
    x = len(i[:-1]) #вычисляем длину каждой строки
    list1.append(x)
#print(list1)
list2 = []
x = int(stroki)
for i in range(1, x + 1): #генерируем список из количества строк файла
    list2.append(i)
#print(list2)
print(f"Количество строк в файле 'text_3.txt': {stroki}")
dict1 = dict(zip((list2), (list1)))
#print(dict1)
print(f'Номер строки и количество символов в ней: {dict1.items()}')