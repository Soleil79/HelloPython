# print('hello world')
# value = None
# print(type(value))
# a = 123
# b = 1.23
# print (type(a))
# print (type(b))
# value = 12334
# print(type(value))
# s = 'hello world'
# print(s) # вывод строки
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)

# # Ввод и вывод данных
# # print, input

# print('введите a')
# a = int(input()) # float - для вещественных значений 1.2 3.5 и т.п.
# print('введите b')
# b = int(input())
# print(a, ' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}') 

# # Арифметические операции
# # +, -, *, /, %, //, **
# # **, +, -, *, /, //, %, +, -
# # (), Сокращенные операции
# a = 12
# b = 8
# c = a % b
# print(c)

# # // деление в целых числах
# # % остаток от деления
# # ** возведение в степень
# # round(a * b, 3) округленине вещественных знаков после переменных указать до скольки знаков

# a = 3
# a += 5
# print(a)

# # Логические операцмм
# # >, >=, <, <=, ==, !=
# # not, and, or - не путать с &, |, ^
# # is, is not, in, not in
# # gen

# f=  [1,2,3,4]

# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2 # 0 - false, 1 - true
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == ' Маша ':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)



# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     # print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

#for

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# r = range(10) # (1, 10, 2)
# for i in r:
#     print(i)

# ecsr

# text = 'съешь еще этих мягких французских булок'
# help(str)
# print(len(text))               # 39
# print('еще' in text)           # True
# print(text.isdigit())          # False
# print(text.islower())          # True
# print(text.replace('еще', 'ЕЩЕ'))   #

# for c in text:
#     print(c)

# text = 'съешь еще этих мягких французских булок'
# print(text[0])                       # с
# print(text[1])                       # ъ
# # print(text[len(text)])               # IndexError
# print(text[len(text)-1])             # к
# print(text[-5])                      # б
# print(text[:])                       # print(text)
# print(text[:])                       # съ
# print(text[len(text)-2])             # ок
# print(text[2:9])                     # ешь еще
# print(text[6:-18])                   # еще этих мягких
# print(text[0:len(text):6])           # сеикакл
# print(text[::6])                     # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

## list = list

# numbers = [1, 2, 3, 4, 5]
# print(numbers)                       # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran) # Приведение типа range к типу list
# print(type(numbers))
# print(numbers)                       # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)                       # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)                         # [20, 4, 6, 8, 10]
# print(numbers)                       # [10, 2, 3, 4, 5]


# colors = ('red', 'green', 'blue')

# for e in colors:
#     print(e)       # red green blue

# for e in colors:
#     print(e*2)      # redred greengreen blueblue

# colors.append('grey') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'grey']) # True
# colors.remove('red') #del colors[0]  # удалить элемент


# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

# arg = 2
# print(f(arg))
# print(type(f(arg)))
