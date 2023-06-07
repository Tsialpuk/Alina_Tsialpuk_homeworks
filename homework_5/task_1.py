"""
Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
Цифры от 1 до 10 отвечают за номера,а от 1 до 2 за цвет (1-красный, 2 - черный).
пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).
В случает неудачи вывести на экран правильную комбинацию.

"""
import random  # запускаем генератор случайного числа в пределах от 1 до 10
num_random = str(random.randint(1, 10))
color_random = random.randint(1, 2)
poputka = 1

if color_random == 1:  #если 1 то присваивается красный цвет, если 2 то черный
    color_random = "красный"
else:
    color_random = "черный"

random_Comb = f"{num_random} {color_random}" #создаем переменную, которая содержит в себе данные которые сгенерированы случайно
print(random_Comb)  #для проверки комбинации
while poputka <= 5:
    num2 = input('введите  число от 1 до 10:')
    color2 = input('введите цвет (красный или черный):')
    num_color2 = f"{num2} {color2}"  # создаем переменную, которая содержит в себе данные которые ввел пользователь
    poputka += 1  #увеличиваем попытку на единицу
    if num_color2 == random_Comb:  #если мы угадали, то заккнчиваем цикл
        print("Вы угадали правильную комбинацию")
        break
    elif poputka > 5:  #если попыток > 5, то выводим выигрышную комбинацию
        print(f"Вы израсходовали попытки.Вот правильная комбинация: {random_Comb}")
    else:
        print(f"Вы не угадали.Сейчас будет {poputka} попытка из 5")



