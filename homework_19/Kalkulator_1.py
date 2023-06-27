"""
1)	Реализовать калькулятор с 4 методами:
Сумма, вычитание , умножение, деление.
Метод принимает 2 аргумента и возвращает результат.
Невалидные данные должны быть обработаны. Валидатором является в программе метод,
 который будет проверять ваши аргументы на то, является ли это число

"""
class Kalkulator:

    def validator(self, num1, num2):
        try:
            if type(num1) == int and type(num2) == int:
                return True
        except ValueError:
            return False

    def sum(self, num1, num2):
        if my_kalkulator.validator(num1, num2):
            return num1 + num2
        else:
            return ValueError("Невалидные данные. Аргументы должны быть числами.")

    def raznica(self, num1, num2):
        if my_kalkulator.validator(num1, num2):
            return num1 - num2
        else:
            return ValueError("Невалидные данные.Введите числа")

    def proizv(self, num1, num2):
        if my_kalkulator.validator(num1, num2):
            return num1 * num2
        else:
            return ValueError("Невалидные данные. Введите числа")

    def delenie(self, num1, num2):
        if my_kalkulator.validator(num1, num2):
                return num1 / num2
        else:
            return ValueError("Невалидные данные. Введите числа.")

my_kalkulator = Kalkulator()
num1 = 2
num2 = 2.5
operation = input('выберете операцию (+,-,*,/)')
if operation == '+':
    print(my_kalkulator.sum(num1, num2))
elif operation == '-':
    print(my_kalkulator.raznica(num1, num2))
elif operation == '*':
    print(my_kalkulator.proizv(num1, num2))
elif operation == '/':
    try:
        print(my_kalkulator.delenie(num1, num2))
    except ZeroDivisionError:
        print('Делить на ноль нельзя. введите другое число')


