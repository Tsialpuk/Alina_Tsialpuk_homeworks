"""
2)	Функция sum(a,b) принимает 2 числа и возвращает их сумму. Написать декоратор,
который возвращает ошибку если переданы не числовые параметры(например строка)
примерно такое:
@validate_int_parameters
def sum(a,b)
sum(3, "1") => ошибка sum(4, 2) = > 6

"""
def validate_int_parameters(func):
    def wrapper(num1, num2):
        if not (isinstance(num1, int) and isinstance(num2, int)):
            return ValueError('Ошибка. Введите числа')
        return func(num1, num2)
    return wrapper


@validate_int_parameters
def sum(num1, num2):
    return num1 + num2
num1 = 5
num2 = '3'
print(f'sum ({num1},{num2}) => {sum(num1, num2)}')