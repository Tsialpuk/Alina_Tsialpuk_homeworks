"""
даны 2 списка: a= [4, 6 ,'py','tell',78] b = [44,'hello',56,'exept',3]
выполнить следующие операции:1) Сложить два списка
2)Добавьте элемнент 6 на 3 позицию.
3) Удалите все текстовые переменные
4) Посчитайте количество элементов списка
"""
a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
print(f'список а:{a}')
print(f'список b: {b}')
slog = a + b
print(f'сложение двух списков: {slog}')
slog.insert(3, 6)
print(f'добавление элемента 6 на 3 позицию: {slog}')
for i in slog:
    if type(i) == str:
        slog.remove(i)
print(f'список без текствовых пременных: {slog}')
len_slog = len(slog)
print(f'количество элементов в списке: {len_slog}')
