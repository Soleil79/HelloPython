# 1. Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.
# print('введите a')
# a = int(input()) 
# print('введите b')
# b = int(input())
# if b == a**2 or a == b**2:
#      print('Yes')
# else: 
#     print ('No')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# max = 0
# for i in range(5):
#     num = int(input())
#     if num > max:
#         max = num
# print(' максимальное число', max)
    
# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# вар.1
# a = int(input('write a number '))
# for i in range(-a, a+1):
#     print(i, end=' ')

# вар.2
# num = int(input())
# neg_num = -num
# while num != neg_num:
#     print(neg_num, end=", ")
#     if num > 0:
#         neg_num += 1
#     else:
#         neg_num -= 1

# 4. Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

# num = float(input('Введите число '))
# a=int(num*10%10)
# if a != 0:
#     print (a)
# else:
#     print('no')

# 5. Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

# a = int(input('Введите число '))
# if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30:
#     print('yes')
# else:
#     print('no')

# (x = z) V (x -> (y /\ z))
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x == z or x <= y and z):
                print(x, y, z)

  