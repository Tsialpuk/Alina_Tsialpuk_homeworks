"""
даны несколько  списков: [-8,1,2,-2,0], [1,-1,0,-9,4,-5], [1,4,0,23,6,34].
Для каждого из списков найти второе наименьшее значение в нем
(правильные ответы выделены жирным шрифтом)
"""
list1 = [-8, 1, 2, -2, 0]
list2 = [1, -1, 0, -9, 4, -5]
list3 = [1, 4, 0, 23, 6, 34]
min1 = min(list1)
min2 = min(list2)
min3 = min(list3)
for i in list1:
    if i == min1:
        list1.remove(i)
        min1_2 = min(list1)
        print(f'Второе наименьшее значение в списке {list1}: {min1_2}')
for i in list2:
    if i == min2:
        list2.remove(i)
        min2_2 = min(list2)
        print(f'Второе наименьшее значение в списке {list2}: {min2_2}')
for i in list3:
    if i == min3:
        list3.remove(i)
        min3_2 = min(list3)
        print(f'Второе наименьшее значение в списке: {list3}: {min3_2}')
