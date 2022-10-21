
from data_import import import_data
from data_export import export_data
from search_data import search_data


def choice():
    print("Выберите действие:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':       
       import_data()
    elif ch == '2':
        export_data()
    else:
        word = input("Введите данные для поиска: ")               
        search_data(word)
        