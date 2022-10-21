# модуль поиска контакта





def search_data(word):
     
    with open('phone_book.csv', 'r', encoding='utf-8') as file:                
        str = list(file.readlines())
        count = 0
        for row in str:
            if word in row:
                print(row)
                count += 1            
        if count <= 0:
            print('Данные не обнаружены')
            
    