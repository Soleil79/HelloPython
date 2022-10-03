# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5


def checkNum(inputText):
    OK = False
    while not OK:
        try:
            number = int(input(f'{inputText}'))
            OK = True
        except ValueError:
            print('Error')        
    return number

def Fibonacci(number):
    if number < 0:
        return 'Введите положительное число'
    a, b = 1, 1
    fib_list = [1,0,1]
    for i in range(1, number):
        a, b = b, a + b
        fib_list.append(a)
        fib_list.insert(0, a * (-1) **i )
    return fib_list         


num = int(checkNum('Введите число: '))
print(Fibonacci(num))


