# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


from random import randint

def checkNum(inputText):
    OK = False
    while not OK:
        try:
            number = int(input(f'{inputText}'))
            if number < 0:
                print('Negative value of the number of numbers!')
                quit()
            OK = True
        except ValueError:
            print('Error') 
        
    return number

def fillList(list):
    NewList = []
    for i in list:
        if list.count(i) == 1:
            NewList.append(i)
    return NewList   
    
num = int(checkNum('Введите количество элементов списка: '))
my_list = [randint(1, num) for x in range(num)]   # Первый список (еще можно было choices(range(10), k=num))
print(my_list)
new_list = fillList(my_list)
print(new_list)

