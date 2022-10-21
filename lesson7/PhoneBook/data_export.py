import csv
def export_data():
    with open('phone_book.csv', 'a+', encoding='utf-8') as file:
       while True:
        name = input('Введите данные сотрудника: Имя, Фамилия, Телефон, Комментарий или введите end: \n')
        if name != 'end':
            file.write(f'{name}\n')
        else:
            break
        file.write('')

