# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import random

def checkNum(inputText):
    OK = False
    while not OK:
        try:
            number = int(input(f'{inputText}'))
            OK = True
        except ValueError:
            print('Error')        
    return number

def fillList(number):
    list = [] 
    for i in range(number):
        new_element = (random() * (number*2 - 1)+1)
        list.append(round(new_element, 2))
    return list
    

def NewList(list):
    new_list = []
    N = len(list)
    for i in range(N):
        new_element = round((((list[i] *100) % 100) / 100), 2)
        new_list.append(new_element)
       
    return new_list

def MaxMinDiff(list): 
    N = len(list)
    i = 0
    max = list[i]
    min = list[i]
    for i in range(N):        
        if list[i] > max:
            max = list[i]
    for i in range(N):         
        if list[i] < min:
            min = list[i]
    diff = round((max - min), 2)
    print(f'max:', max, '   min:', min)       
    return diff  
    
    
num = int(checkNum('Введите количество элементов списка: '))
my_list = fillList(num)
print(my_list)
remainder_list = NewList(my_list)
# print(remainder_list)
print(f'Разница между максимальным и минимальным значением дробной части элементов: ', MaxMinDiff(remainder_list))
