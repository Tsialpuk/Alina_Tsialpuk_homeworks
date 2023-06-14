"""
9.	Дан список [student_1, student_2, student_3] с
помощью цикла for добавить к каждому элементу списка слово “_good”. Вывести на экран.
"""
list1 = ["student1", "student2", "student3"]
list2 = []
for element in list1:
    list2.append(element + "_good")
print(list2)
