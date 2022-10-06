# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0


from random import randint, choice
import weakref

def checkNum(inputText):
    OK = False
    while not OK:
        try:
            number = int(input(f'{inputText}'))
            OK = True
        except ValueError:
            print('Error') 
        
    return number

def Polinomial(num):
    with open('poli.txt', 'a', encoding='utf-8') as my_file:       
        for i in range(num+1): 
            new_coenf = randint(0, 10)
            sign = choice('+-')
            if num >= 1:                
                if new_coenf != 0:
                    my_file.write(f'{new_coenf}*x^{num} {sign} ')
                    num -= 1
                else:
                    my_file.write(f'')
                    num -= 1
            else:
                my_file.write(f'{new_coenf} = 0\n')
                
        my_file.write('')

def Polinomial2(num): # Для создания второго файла
    with open('poli2.txt', 'a', encoding='utf-8') as my_file2:       
        for i in range(num+1): 
            new_coenf = randint(0, 10)
            sign = choice('+-')
            if num >= 1:                
                if new_coenf != 0:
                    my_file2.write(f'{new_coenf}*x^{num} {sign} ')
                    num -= 1
                else:
                    my_file2.write(f'')
                    num -= 1
            else:
                my_file2.write(f'{new_coenf} = 0\n')
                
        my_file2.write('')

print('создадим первый файл:')
for i in range(3):           
    number = int(checkNum('Введите степень k: '))
    Polinomial(number)
    
print()

print('создадим второй файл:')
for i in range(3):      # Для создания второго файла     
    number2 = int(checkNum('Введите степень k: '))
    Polinomial2(number2)
    