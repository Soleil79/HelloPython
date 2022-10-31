
from data_view import *
from logger import * 


read_data()

def userName():
    user = input('Для доступа к базе данных введите ваше имя: ') # Для логирования и записи в журнал 
    return user


def choice():
    print("Выберите действие:\n\
    1 - Показать все записи;\n\
    2 - Найти сотрудника по параметру;\n\
    3 - Добавить нового сотрудника; \n\
    4 - Изменить запись; \n\
    5 - Удалить запись; \n")
    ch = input("Введите цифру: ")

    if ch == '1':
        my_user = userName()
        show_data()
        access_logger('Show all', my_user) 

    elif ch == '2':
        my_user = userName()
        print('Выберите параметр поиска: \n\
        1 - фамилия; \n\
        2 - имя; \n\
        3 - должность; \n\
        4 - зарплата; \n')
        ch = input('Введите цифру: ')
        if ch == '1': search_data(str.capitalize(input('Введите фамилию сотрудника: \n')))
        elif ch == '2': search_data(str.capitalize(input('Введите имя сотрудника: \n')))
        elif ch == '3': search_data(str.lower(input('Введите должность сотрудника: \n')))
        elif ch == '4': search_data(input('Введите зарплату сотрудника (тыс.руб): \n'))
        else:  ErrorMessage()
        access_logger('Search an emploee', my_user)
            
    elif ch == '3':
        my_user = userName()
        my_dict = {'id':'', 'surname':'', 'name': '', 'position':'', 'salary':'', 'phone':''}
        for i in my_dict:
            if i != 'id':
                print('Введите данные по сотруднику:')
                my_dict[i] = input(f'Введите {i}: ')
        new_employee(my_dict)
        access_logger('Add an employee', my_user)

    elif ch == '4':
        my_user = userName()
        show_data()
        choose = int(input('Что хотите поменять: \n\
            1 - фамилия; \n\
            2 - имя; \n\
            3 - должность; \n\
            4 - зарплата; \n\
            5 - телефон; \n'))
        if choose in range(6):      
            keys = {1:'surname', 2: 'name', 3: 'position', 4: 'salary', 5: 'phone'}
            change_data(input('Введите ID сотрудника: '), keys[int(choose)])
        else: ErrorMessage()
        access_logger('Change data', my_user)
    
    elif ch == '5':
        my_user = userName()
        show_data()
        delete_data(input('Введите ID сотрудника: ')) 
        access_logger('Delete an employee', my_user)        
    
    else:
        ErrorMessage()
        
def ErrorMessage():
    print('Вы ввели не корректные данные! Нажмите Enter чтобы вернуться в главное меню или напишите end: ')
    user_ch = input('')
    if user_ch != 'end':
        choice()
    
        