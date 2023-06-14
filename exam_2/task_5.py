"""
5)Есть словарь песен группы Depeche Mode violator songsdict = { 'World in

My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88,
'Blue Dress': 4.18, 'Clean': 5.68, }
 Выведите общее время звучания всех песен.
 Создайте список песен, время звучаниях которых больше 5 минут Создайте новый словарь тех песен,
  в название которых состоит из одного слова

"""
songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88,
'Blue Dress': 4.18, 'Clean': 5.68}
list_1 = []
list_2 = []
list_3 = []
sum = 0
songsdict_1 = {}
for key, value in songsdict.items():
    sum += value
    if value > 5.0:
        list_1.append(key)
    if len(key.split()) == 1:
        list_2.append(key)
        list_3.append(value)
    songsdict_1 = dict(zip(list_2, list_3))
print(f'Общее время звучания всех песен: {sum}')
print(f'Список песен длительность звучания которых больше 5 минут {list_1}')
print(f'словарь  из тех песен название которых состоит из одного слова{songsdict_1}')