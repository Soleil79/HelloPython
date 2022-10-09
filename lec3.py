#!!! lambda !!!

# def f(x):
#     return x**2

# print(f(2))

# def calc(x):
#     return x+10
# print(calc(10))

# def calc2(x):
#     return x*10
# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)


# ---------------------


# from ast import comprehension


# def sum(x, y):
#     return x+y

# # f = sum
# sum = lambda x, y: x+y

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#     # return op(a,b)

# # calc(mylt, 4, 5)
# # calc(f, 4, 5)
# # calc(sum, 4, 5)
# calc(lambda x, y: x+y, 4, 5)

# --------------------------------


# !!! List comprehension !!!
  
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# list = []

# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)

# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# # list = [i for i in range(1, 21) if i%2 == 0]
# # list = [(i, i) for i in range(1, 21) if i%2 == 0] # кортежи

# print(list)

# ---------------------------------

# К чему это всё?
# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# path ='/Users/sergejkamaneckij/Projects/python/Lecture003/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e **2))
# print(out)

# Упрощаем код, используя лямбду:

# def select (f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data) #  или map(int, data)
# res = where(lambda x: not x % 2, res) # или filter(lambda...)
# res = select(lambda x:(x, x**2), res) # или list(map(lambda...))
# print(res)

#---------------------------------------------


# !!! Функция map !!!
# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
#  ↓ ↓ ↓ ↓ ↓
#  [ 11, 12, 13, 14, 15]
# Нельзя пройтись дважды

# li = [x for x in range(1,20)]
# li = list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)

# for e in data:
#     print(e)

#-------------------------------------

# !!! Функция filter !!!
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#  ↓
#  [ 2, 4 ]
# Нельзя пройтись дважды

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2, data))
# print(res)

# --------------------------------------------


# !!! Функция zip !!!


# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data)

#------------------------------------------

# !!!! Функция enumerate !!!

# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# data = list(enumerate(users))
# print(data)


# ИТОГИ:
# Как упростить работу с данными
# Научились map, filter, zip
# List comprehensions,
# enumerate,
# анонимные \ lambda функции
# Как улучшить
# программу, написанную в предыдущей лекции?