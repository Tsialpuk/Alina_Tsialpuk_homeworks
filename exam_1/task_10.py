"""
10.	Вывести на экран числа от 0 до 50, кроме 35.
"""
#1 способ
for i in range(0, 50):
    if i == 35:
        continue
    print(i)
#2 способ
"""
list2 = []
for i in range(0, 50):
    list2.append(i)
    if i == 35:
        list2.remove(i)
print(list2)
"""