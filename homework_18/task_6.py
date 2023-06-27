"""
6.	Напишите функцию для сортировки слов в алфавитном порядке
"""
def sort_words(words):
    sorted_words = sorted(words)
    return f"Отсортированные слова в алфавитном порядке: {sorted_words}"

print(sort_words(['my', 'name', 'is', 'alina']))