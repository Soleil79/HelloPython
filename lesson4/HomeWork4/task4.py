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

def fillList(num):
    for i in range(num):
        new_coenf = randint(-10, 10) in range(num) 
        

      
    
num = int(checkNum('Введите степень k: '))
new_coenf = randint(-10, 10) in range(num)   # Первый список (еще можно было choices(range(10), k=num))
print(new_coenf*x^num, + )
new_list = fillList(my_list)
print(new_list)

# a, b, c = (int(input()) for _ in range(3))
