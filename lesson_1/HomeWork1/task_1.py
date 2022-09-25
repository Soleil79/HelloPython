# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print('введите день недели ')
day = int(input()) 
if day in range(1,6):
     print('Workday')
elif day in range(6,8): 
    print ('Weekend')
else:
    print ("It's not a day of the week!")