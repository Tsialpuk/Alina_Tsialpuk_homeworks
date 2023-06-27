"""
5.	Функция для определения того, является ли строка палиндромом
"""
def string_palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    reversed_string = string[::-1]
    if string == reversed_string:
        return f"Строка '{string}' является палиндромом"
    else:
        return f"Строка '{string}' не является палиндромом"


print(string_palindrome('was it a car or a cat I saw'))
print(string_palindrome('My name is Alina'))
