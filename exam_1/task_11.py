"""
11.	Дан список [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
В новый список добавить элементы, которые содержат пробел.
"""
list1 = ["hello my friend", "my name is", "house", "cat", "dog"]
list2 = []
for i in list1:
    if not i.isalpha():
        list2.append(i)
print(list2)
"""
#2 способ
my_list = ["hello my friend", "my name is", "house", "cat", "dog"]
new_list = []
for i in my_list:
    if ' ' in i:
        new_list.append(i)
print(new_list)
"""
#3способ
my_list = ["hello my friend", "my name is", "house", "cat", "dog"]
new_list = []
for i in my_list:
    if i.count(' '):
        new_list.append(i)
print(new_list)
