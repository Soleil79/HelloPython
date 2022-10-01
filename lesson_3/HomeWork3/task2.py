# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from ast import Try
from random import sample

def Products (count):
    my_list = sample(range(1, count*2), count)   # Первый список
    print(my_list)
    N = len(my_list)
    NewList = []    # Новый список, состоящий из произведений крайних элементов первого
    if N %2 ==0:   # Проверка первого списка на четность количества элементов
        for i in range(N//2):
            NewList.append(int(my_list[i] * my_list[N-1])) 
            N -= 1
    else: # для списка с нечетным количеством элементов
        for i in range((N//2)+1):    
            if i < N-1:
                NewList.append(int(my_list[i] * my_list[N-1])) 
                N -= 1
            else:
                NewList.append(int(my_list[i] * 1))
    return NewList
    
try: # Проверка на то, что введено именно число integer. 
    num = int(input('Введите количество элементов списка: '))
    print('Произведение пар чисел списка: ', Products(num), end=' ')
except ValueError:
    print('Error')

