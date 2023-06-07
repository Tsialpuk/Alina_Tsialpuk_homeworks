"""
Разделить строку "Apples, Orange, Pears, Bananas, Berries" по запятым
и вывести на экран. Затем объединить элементы с использованием пробела, чтобы программа вывела
"Apples Oranges Pears Bananas Berries".
"""
string1 = '"Apples, Orange, Pears, Bananas, Berries"'
string1_split = string1.split(",")
print(string1_split)
string1_join = " ".join(string1_split)
print(string1_join)
