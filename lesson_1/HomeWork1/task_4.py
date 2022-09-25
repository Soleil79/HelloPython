
# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('введите номер четверти ')
Q = int(input()) 

if Q == 1:
     print('x > 0, y > 0')
elif Q == 2: 
    print ('x < 0, y > 0')
elif Q == 3: 
    print ('x < 0 and y < 0')
elif Q == 4:
    print ('x > 0, y < 0')
else:
    print('The quarter is entered incorrectly!')
