#Вычислить сумму цифр случайного трёхзначного числа
#1способ
a = int(input("Введите трехзначное число: "))
b = a % 10 #вычисляем последнюю цифру трехзначного числа
c = a % 100 // 10 #вычисляем вторую цифру числа
d = a // 100 #вычисляем первую цифру трехзначного числа
print("Сумма цифр трехзначного числа:", b + c + d)
#второй способ
import random #запускаем генератор случайного трехзначного числа в пределах от 100 до 999
a1 = int(random.randint(100, 999))
print("Случайно сгенерированное трехзначное число:", a1)
b1 = a1 % 10 #вычисляем последнюю цифру трехзначного числа
c1 = a1 % 100 // 10 #вычисляем вторую цифру числа
d1 = a1 // 100 #вычисляем первую цифру трехзначного числа
print("Сумма цифр случайно сгенерированного трехзначного числа:", b1 + c1 + d1)



