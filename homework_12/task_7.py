"""
7) Есть строка со знаками препинания. Удалить из строки знаки препиныния.
"""
str_1 = input('введите строку со знаками препинания:')
str_new = str_1.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ').\
    replace(':', ' ').replace('/', ' ').replace('(', ' ').replace(')', ' ').replace(';', ' ').\
    replace('-', ' ').replace('_', ' ').replace('"', ' ')
print(str_new)
#посторалась учесть все знаки препинания, но, возможно что-то забыла