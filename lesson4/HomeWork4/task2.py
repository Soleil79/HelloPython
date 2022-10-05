# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650
# out
# [2, 5, 5, 13]

def checkNum(inputText):
    OK = False
    while not OK:
        try:
            number = int(input(f'{inputText}'))
            OK = True
        except ValueError:
            print('Error')        
    return number

def Factors(num):
    list = []
    simple = 2
    while num > 1:
        if num % simple == 0:
            list.append(simple)
            num = num/simple
        else:
            simple += 1
    return list

N = int(checkNum('Введите число, для нахождения всех его простых множителей: '))
print(Factors(N))
