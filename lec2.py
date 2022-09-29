# !!! ФАЙЛЫ !!!
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+
# 
# 
# with open('file.txt', 'a') as data: # data close не нужен
#     data.write('line 1111\n')
#     data.write('line 2222\n')

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# # data.writelines(colors) # разделителей не будет
# data.write('LINE 1211\n') # \n - переход на новую строку
# data.write('LINE 1311\n')
# data.close()

# exit() #Функция, которая позволяет не выполнять нижеследующтй код
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()



# !!! ФУНКЦИИ !!!

# Это фрагмент программы, используемый
# многократно
# def function_name(x):
    # # body line 1
    # # . . .
    # # body line n
    #  # optional return

# import lec as l # Обращаемся к функции из файла предыдущей лекции (lec.py)
# print(l.f(1))


# def new_string(symbol, count): # (символ, число)
#     return symbol * count   # В Пайтоне мы можем перемножать строку на число

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required 


# def new_string(symbol, count = 3): # (символ, число) можно задать сразу значение count
#     return symbol * count   # В Пайтоне мы можем перемножать строку на число

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string('4')) # 12


# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# !!! КОРТЕЖИ !!!

# Кортеж – это неизменяемый “список”

# a = (3, 1, 41, 4) 
# # Кортеж из одного элемента должен быть с запятой: a = (3,)
# print(a)
# print(a[-2])
# # a[0] = 12 # Error! Для кортежей такое присваивание невозможно



# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support item assignment

# # Распаковка кортежа в отдельные переменные
# t = tuple(['red', 'green', 'blue']) # Создаем список, конвертируем его в кортеж
# red, green, blue = t # распаковываем кортеж в 3 отдельные переменные
# print('r:{} g:{} b:{}'.format(red, green, blue)) # работаем с этими переменными
# # r:red g:green b:blue

# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')


# !!! СЛОВАРИ !!!


# Неупорядоченные коллекции произвольных
# объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',   # Создаем пары: ключ и значение
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться

# for k in dictionary.keys(): # Посмотрим коллекцию ключей (keys), значений (values)
#     print(k)



# print(dictionary['up']) # ↑
# # типы ключей могут отличаться

# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента

# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →


# !!! МНОЖЕСТВА !!!
# Неупорядоченная совокупность элементов. 
# Тип данных: Set


# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

#  # Операции со множествами
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

# # Неизменяемое множество
# # a = {1, 2, 3, 5, 8}
# # b = frozenset(a)
# # print(b) # frozenset({1, 2, 3, 5, 8})

# !!! СПИСКИ !!!

# list1 = [1,2,3,4,5] 
# list2 = list1

# list1[0] = 123 # При вненсении изменений в один список данные меняются и в другом
# list2[1] = 333
 
# print()

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

list1 = [1,2,3,4,5]
# Удаление элемента из списка
# print(len(list1))
# print(list1.pop()) # Метод pop удаляет последний элемент списка
# print((list1))
# print(list1.pop())
# print((list1))
# print(list1.pop())
# print((list1))
# # Удаление заданного элемента
# print(list1.pop(2))
# print((list1))

# Добавление элемента в список
print(list1.insert(2, 11)) # добавление элемента, на позиции индекса 2.
print(list1)

# Добавление элемента в конец списка
print(list1.append(11)) # добавление элемента, на позиции индекса 2.
print(list1)