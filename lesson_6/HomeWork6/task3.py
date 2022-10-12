# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, 
# начинающиеся с соответствующей буквы. 
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def names_list ():
    names = []
    for i in input('Введите имена сотрудников через пробел: ').split():  # В данной записи не нужно ограничивать ввод заданным количеством
        names.append(i)  
    return names

def keys_gen (list):
    letters = []
    for i in list:
        for j in i:
            letters.append(j)
            break
    return letters       
     
def fill_dict(tuple):
    my_dict = {}
    for k, v in tuple:
        my_dict.setdefault(k, []).append(v)
    return my_dict



names = names_list() # Заполняем список с именами
print(names)

keys = keys_gen(names) # выделяем первую букву и формируем список для ключей
# print(keys)

names_tuple = list(zip(keys, names)) # Создаем кортеж из двух списков
# print(names_tuple)

names_dict = fill_dict(names_tuple) # Создаем словарь из кортежа, с объединением элементов с одинаковыми ключами в списки.
sorted_dict = dict(sorted(names_dict.items())) # Сортровка приводит к преобразованию в список, поэтому возвращаем его в словарь при помощи dict
print(sorted_dict)
