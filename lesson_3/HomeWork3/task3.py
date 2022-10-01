# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

# Когда делимое четное, двоичный остаток будет равен 0, а когда делимое нечетное, то двоичный остаток будет равен 1.

import string

def checkNum(inputText): # В этой задаче проверку на ввод числа вывожу в отдельный метод
    OK = False
    while not OK:
        try:
            number = int(input(f'{inputText}'))
            OK = True
        except ValueError:
            print('Error')        
    return number

def FillList(num): # Переводим число из десятичной системы в двоичную, посредством последовательного деления заданного числа на 2. Результат представим в виде списка
    my_list = []
    while num > 0:  
        if num % 2 == 0:
            my_list.append(0)
        else:
            my_list.append(1)
        # print(num)
        num //= 2  
    return my_list  
  
def listReverse(my_list): # Разворачиваем список
    N = len(my_list)
    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[N-1])
        N -= 1
    return new_list
      

decimal_num = int(checkNum('Введите десятичное число: '))
bit_list = FillList(decimal_num)
# print(bit_list)
print(f'Число {decimal_num} в двоичной системе счисления равно: ')
print(''.join(map(str, listReverse(bit_list)))) #Поскольку методы join() принимают только строковые значения,
                                                # мы используем map() для преобразования значений int в строку 
                                                # перед преобразованием списка в строку.

