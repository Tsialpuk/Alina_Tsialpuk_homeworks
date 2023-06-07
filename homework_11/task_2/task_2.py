"""
2)	Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
Окончанием ввода пусть служит пустая строка.
"""
list1 = []
while True: #запускаем цик для ввода данных пользователем
    str1 = input('введите строку:')
    if str1 == (''):
        print('принудительная остановка')
        break
    list1.append(str1)
with open('text_2.txt', 'w', encoding='utf8') as file:
    for i in list1:
        file.write(i + "\n")
with open("text_2.txt", "r", encoding='utf8') as file:
    elements = file.read()
    print(elements)