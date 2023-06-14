"""
15.	Необходимо удалить пустые строки из списка строк.
"""
list1 = ["hello", "world", "", "my", "name", "", "is"]
print(list1)
for i in list1:
    if i == "":
        list1.remove(i)
print(list1)