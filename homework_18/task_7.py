"""
7.	Напишите функцию, которая определяет количество гласных в строке
"""
def count_glass(string):
    glass_1 = 'уеыаоэяиюaёУЕЫАОЭЯИЮЁeiouyAEIOUY'
    count = 0
    for glass in string:
        if glass in glass_1:
            count += 1
    return f"Количество гласных в строке '{string}' равно: {count}"



print(count_glass('My name is Alina, Меня зовут Алина'))