"""
4.	Функция для определения всех чисел, на которые без остатка делится указанное
"""
def delenie_bez_ostatka(num):
    list_1 = []
    for i in range(1, num + 1):
        if num % i == 0:
            list_1.append(i)
    return f"Числа, на которые число {num} делится без остатка: {list_1}"



print(delenie_bez_ostatka(105))
print(delenie_bez_ostatka(33))
