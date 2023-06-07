#Определить существование треугольника

storona1 = int(input("Введите длину первой стороны: "))
storona2 = int(input("Введите длину второй стороны: "))
storona3 = int(input("Введите длину третей стороны: "))
if storona1 + storona2 > storona3 and storona2 + storona3 > storona1 \
        and storona3 + storona1 > storona2:
    #условие присутствия треугольника  сумма двух любых сторон должна быть больше третьей стороны
    print(f"Фигура является треугольником")
else:
    print(f"Фигура не является треугольником")