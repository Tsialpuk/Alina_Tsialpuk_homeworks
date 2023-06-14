"""
3)Создайте словарь
из строки ' An apple a day keeps the doctor away' следующим образом:
в качестве ключей возьмите символы строки, а значениями пусть будут числа,
соответствующие количеству вхождений данной буквы в строку.

"""
str_1 = 'An apple a day keeps the doctor away'
list_1 = list(str_1)
list_2 = []
print(list_1)
for i in str_1:
    x = str_1.count(i)
    list_2.append(x)
dict1 = dict(zip(list_1, list_2))
print(dict1)


