"""
1.	Написать 12 функций по переводу:
1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты
Написать программу, со следующим интерфейсом: пользователю предоставляется
на выбор 12 вариантов перевода(описанных в первой задаче).
Пользователь вводит цифру от одного до двенадцати.
После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого задания.
 Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
"""
def inches_in_sm(inches): #1.дюймы в сантиметры
    return inches * 2.54
def sm_in_inches(sm): #2.сантиметры в дюймы
    return sm * 0.394
def mile_in_km(mile): #3.мили в киллометры
    return mile * 1.609
def km_in_mile(km): #4.киллометры в мили
    return km * 0.621
def pound_in_kilo(pound): #5.фунты в килограмы
    return pound * 0.454
def kilo_in_pound(kilo): #6.килограмы в фунты
    return kilo * 2.205
def ounce_in_gram(ounce): #7.унции в граммы
    return ounce * 28.35
def gram_in_ounce(gram): #8.граммы в унции
    return gram * 0.0353
def gallon_in_liter(gallon): #9.галлоны в литры
    return gallon * 3.785
def liter_in_gallon(liter): #10литры в галоны
    return liter * 0.2642
def pint_in_litter(pint): #11пинты в литры
    return pint * 0.473
def litter_in_pint(liter): #12литры в пинты
    return liter * 2.113
while True:
    print("1. Дюймы в сантиметры")
    print("2. Сантиметры в дюймы")
    print("3. Мили в километры")
    print("4. Километры в мили")
    print("5. Фунты в килограммы")
    print("6. Килограммы в фунты")
    print("7. Унции в граммы")
    print("8. Граммы в унции")
    print("9. Галлон в литры")
    print("10. Литры в галлоны")
    print("11. Пинты в литры")
    print("12. Литры в пинты")
    print("введите 0 для выхода из программы")
    choice = int(input("Выберете тип перевода:"))
    if choice == 0:
        break
    znacinie = float(input("Введите значение"))
    if choice == 1:
        result = inches_in_sm(znacinie)
        print(f"{znacinie} дюймов равно {result} сантиметров")
    elif choice == 2:
        result = sm_in_inches(znacinie)
        print(f"{znacinie} сантиметров равно {result} дюймов")
    elif choice == 3:
        result = mile_in_km(znacinie)
        print(f"{znacinie} миль равно {result} километров")
    elif choice == 4:
        result = km_in_mile(znacinie)
        print(f"{znacinie} километров равно {result} миль")
    elif choice == 5:
        result = pound_in_kilo(znacinie)
        print(f"{znacinie} фунтов равно {result} килограмм")
    elif choice == 6:
        result = kilo_in_pound(znacinie)
        print(f"{znacinie} килограмм равно {result} фунтов")
    elif choice == 7:
        result = ounce_in_gram(znacinie)
        print(f"{znacinie} унций равно {result} грамм")
    elif choice == 8:
        result = gram_in_ounce(znacinie)
        print(f"{znacinie} грамм равно {result} унций")
    elif choice == 9:
        result = gallon_in_liter(znacinie)
        print(f"{znacinie} галлонов равно {result} литров")
    elif choice == 10:
        result = liter_in_gallon(znacinie)
        print(f"{znacinie} литров равно {result} галонов")
    elif choice == 11:
        result = pint_in_litter(znacinie)
        print(f"{znacinie} пинт равно {result} литров")
    elif choice == 12:
        result = litter_in_pint(znacinie)
        print(f"{znacinie} литров равно {result} пинт")


