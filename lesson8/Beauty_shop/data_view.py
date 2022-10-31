import csv

csv_bd = []
id_count = 0


def read_data():
    global csv_bd
    global id_count
    with open('Beauty_shop.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            csv_bd.append(row)
            if int(row['id']) > id_count:
                id_count = int(row['id']) 
    
 

def show_data():
    global csv_bd, id_count       
    print('СПИСОК СОТРУДНИКОВ:\nid, Фамилия, Имя, Должность, Зарплата(тыс.руб.), Телефон:')
    print('---------------------------------------------------------')
    for row in csv_bd:
        print(", ".join(row.values()))   
    print('')
  

def search_data(word):
    global csv_bd
    count = 0
    for row in csv_bd:        
        if word in row.values():   
            print(", ".join(row.values()))
            count += 1            
    if count <= 0:
        print('Данные не обнаружены')
    

def new_employee(new_data):
    global id_count    
    new_id_count = id_count + 1
    new_data['id'] = new_id_count
    print(new_data)
    with open('Beauty_shop.csv', 'a', encoding='utf-8') as file:
        field_names = ['id', 'surname', 'name', 'position', 'salary', 'phone']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writerow(new_data)
    print('Добавление нового сотрудника прошло успешно')
    

def change_data(id_change, key_change):
    global csv_bd    
    for i in csv_bd:
        if id_change == i['id']:
            i[key_change] = input('Введите новые данные: ')
            break
    with open('Beauty_shop.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'surname', 'name', 'position', 'salary', 'phone'])
        writer.writeheader()
        for j in csv_bd:
            writer.writerow(j)
    print('Данные успешно изменены')
            
    

def delete_data(id_del):
    global csv_bd
    global id_count    
    new_bd = []
    for i in csv_bd:
        if id_del != i['id']:
            new_bd.append(i)
    
            with open('Beauty_shop.csv', 'w', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'surname', 'name', 'position', 'salary', 'phone'])
                writer.writeheader()
                id_count = 1
                for j in new_bd:
                    j['id'] = id_count 
                    writer.writerow(j)
                    id_count += 1
        else:
            print(f'Сотрудник c ID {id_del} успешно удален из базы.')
    csv_bd = new_bd
    
