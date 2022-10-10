# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def checkNum(inputText):
    OK = False
    while not OK:
        try:
            number = int(input(f'{inputText}'))
            if number < 0:
                print('The data is incorrect!')
                quit()
            OK = True
        except ValueError:
            print('Error') 
        
    return number

def FillList(n, word):
    list = []
    for i in range(n):
        a = sample(word, k=3)
        list.append(''.join(a))
    return list

def DeleteWord(list):
    new_list = []
    for i in range(len(list)):
        if list[i] != ('абв'):
            new_list.append(list[i])
    return new_list

count = int(checkNum('Введите количество элементов: '))
WordList=FillList(count, 'абв')
print(WordList)
print(DeleteWord(WordList))

# num = int(checkNum('Введите количество элементов списка: '))
# my_list = [randint(1, num) for x in range(num)]   # Первый список (еще можно было choices(range(10), k=num))
# print(my_list)
# new_list = fillList(my_list)
# print(new_list)
