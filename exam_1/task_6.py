"""
6.	В строке “Иван Иванов” поменяйте местами слова.
Может быть предоставлена любая строка с именем и фамилией.
например
“Петр Иванов” => “Иванов Петр”

"""
name_surname = str(input('Введите ваше имя и фамилию'))
name_surname_new = name_surname.split(" ")
print(name_surname_new[-1], name_surname_new[-2])

#2 способ
string = 'ivan ivanov'
string_split = string.split(' ')
string_list = list(reversed(string_list))
print(string_join)