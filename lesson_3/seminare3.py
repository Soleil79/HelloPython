 # 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая определит, присутствует ли в заданном списке число,
# полученное от пользователя.

# from random import sample

# def num_in_list(count, number):
#     if count < 0:
#         return "Error"
#     my_list = sample(range(1, count *2), count)
#     print(my_list)
#     if number in my_list:
#         return "Yes"
#     return "No"
# print(num_in_list(int(input()), int(input())))

# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.

from random import choices, sample

def list_new(n, word):
    new_list = []
    for i in range(n):
        a = choices(word, k=3)
        new_list.append(''.join(a))
    return new_list

def list_search(my_list, key):
    if my_list.count(key) >1:
        print("Yes")
        n=my_list.index(key)
        print(my_list.index(key, n+1))
    else:
        print(-1)
result=list_new(10, 'abc')
print(result)
list_search(result, input())

sample