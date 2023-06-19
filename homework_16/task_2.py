"""
Создайте программу, которая, принимая массив имён, возвращает строку описывающая
количество лайков (как в Facebook). Примеры:
likes() -> "no one likes this"
likes("Ann") -> "Ann likes this"
likes("Ann", "Alex") -> "Ann and Alex like this"
likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"
"""
def Facebook_likes(names):
    likes = len(names)
    if len(names) == 0:
        return 'no one likes this'
    elif likes == 1:
        return names[0] + ' likes this'
    elif likes == 2:
        return ' and '.join(names) + ' like this'
    elif likes == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        return names[0] + ', ' + names[1] + ' and ' + f' {str(likes-2)} other like this'

print(Facebook_likes([]))
print(Facebook_likes(['Ann']))
print(Facebook_likes(['Ann', 'Alex']))
print(Facebook_likes(['Ann', 'Alex', 'Mark']))
print(Facebook_likes(['Ann', 'Alex', 'Mark', 'Max']))