"""
5)	Выведите статистику частности букв в кортеже
long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и’,'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и’)
Примечание: Статистика частности - число повторений каждой из букв.

"""
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')
print(f"исходный кортеж: {long_word}")
print(f"частность повторений буквы 'т': {long_word.count('т')}")
print(f"частность повторений буквы 'а': {long_word.count('а')}")
print(f"частность повторений буквы 'и': {long_word.count('и')}")
