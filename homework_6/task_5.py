"""
Заполнить список ста нулями, кроме первого и последнего элементов,
которые должны быть равны единице
"""
list1 = []
for i in range(100):
    list1.append(0)
list1[0] = 1
list1[-1] = 1
print(list1)
#x = len(list1) №для проверки длины списка
#print(x)