# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import choices

def checkNum(inputText):
    OK = False
    while not OK:
        try:
            number = int(input(f'{inputText}'))
            if number < 0:
                print('Negative value!')
                quit()
            OK = True
        except ValueError:
            print('Error') 
        
    return number

def fillList(list):
    NewList = [list[i+1] for i in range(len(list)-1) if list[i+1] > list[i]]         
    return NewList 

# def fillList(list):
#     NewList = []
#     for i in range(len(list)-1):
#         if list[i+1] > list[i]:
#             NewList.append(list[i+1])          
#     return NewList 

num = int(checkNum('Введите количество элементов списка: '))
my_list = choices(range(num*3), k=num)   
print(my_list)
new_list = fillList(my_list)
print(new_list)