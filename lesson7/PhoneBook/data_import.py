# модуль экспорта данных 
import csv

def import_data():
   
    with open('phone_book.csv', 'r', encoding='utf-8') as file:  
        file_reader = csv.reader(file)
        for row in file_reader:
            print(row)
                            
        return file_reader

print(import_data)


