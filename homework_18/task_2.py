"""
2.	Написать функцию date, принимающую 3 аргумента — день, месяц и год.
Вернуть True, если такая дата есть в нашем календаре, и False иначе.
"""
def data(day, month, year):
    if  day > 31 and  month > 12 and  year < 1:
        return f'Дата: {day}, {month}, {year}  не существует'
    if month in {4, 6, 9, 11}:
        if day < 1 or day > 30:
            return f'Дата {day}, {month}, {year} не существует'
        else:
            if day < 1 or day > 31:
                return f'Дата {day}, {month}, {year} не существует'
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day < 1 or day > 29:
                return f'Дата {day}, {month}, {year} не существует'
        else:
            if day < 1 or day > 28:
                return f'Дата {day}, {month}, {year} не существует'

    return f'Дата {day}, {month}, {year} существует'

day = int(input('введите день:'))
month = int(input(('Введите месяц')))
year = int(input('Введите год'))
print(data(day, month, year))
