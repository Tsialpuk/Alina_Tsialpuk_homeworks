"""
12.	В классе N школьников. На уроке физкультуры тренер говорит «на первый-второй рассчитайтесь».
Выведите, что скажут ученики.
Входные данные: Вводится одно целое число — количество человек в классе.
Входные данные: Выведите последовательность чисел 1 и 2, в том порядке,
как будут говорить школьники.

"""
n = int(input('Введите количество учеников в классе:'))
poputka = 1
list1 = [i for i in range(1, n+1)]
if poputka <= n:
    for i in list1:
        if i % 2 != 0:
            i = "первый!"
            print(i)
        else:
            i = "второй!"
            print(i)
else:
    print('расчет окончен')


#2 способ