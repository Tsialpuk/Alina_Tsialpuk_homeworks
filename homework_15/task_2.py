"""
Если в функцию передается кортеж, то посчитать длину всех его слов.
Если список, то посчитать кол-во букв и чисел в нем.
 Число - количество нечетных цифр. Строка - количество букв.
"""

def len_letters_numbers(text):
    if type(text) == tuple:
        len_words_tuple = sum(len(str(i)) for i in text if isinstance(i, str))
        print(f'Длина всех слов кортежа: {len_words_tuple}')
    elif type(text) == list:
        letters = 0
        numbers = 0
        for i in text:
            if type(i) == str:
                letters += len(i)
            elif type(i) == int:
                numbers += 1
        print(f'Количество чисел в списке: {numbers}')
        print(f'Количество букв в списке: {letters}')
    elif type(text) == int:
        necet = 0
        for i in str(text):
            if int(i) % 2 != 0:
                necet += 1
        print(f'Количество нечетных цифр в числе: {necet}')
    elif type(text) == str:
        letters_2 = 0
        for i in text:
            if i.isalpha():
                letters_2 += 1
        print(f'Количество букв в строке: {letters_2}')


len_letters_numbers((1, 2, 3, 7, 'hello', 'my', 'name', 9, 2, 'is', 6))
len_letters_numbers([1, 2, 3, 7, 'hello', 'my', 'name', 9, 2, 'is', 6])
len_letters_numbers(1234567891)
len_letters_numbers('hello my name is')
















