# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8

from ast import Try
from random import sample

def SumOdds (count):
    my_list = sample(range(1, count*2), count)
    print(my_list)
    sum = 0
    for i in range(count): 
        if i%2==0:
            sum += my_list[i]
    return sum
  

try: # Проверка на то, что введено именно число integer. 
    num = int(input('Введите количество элементов списка: '))
    print('Сумма элементов, стоящих на нечетных позициях равна:', SumOdds(num))
except ValueError:
    print('Error')



