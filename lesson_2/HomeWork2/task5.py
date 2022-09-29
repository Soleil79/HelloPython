# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]


import random


n = int(input('Введите количество элементов массива: '))
nums=list(range(n))
print(nums)

def mix_list(list_old):
    # Создаем новый список, поскольку мы не должны изменять оригинал
    list = list_old[:]
    # Цикл от 0 до длины списка -1
    list_length = len(list)
    for i in range(list_length):
        # Получение случайного индекса
        random_index = random.randint(0, list_length - 1)
        # Замена
        temp = list[i]
        list[i] = list[random_index]
        list[random_index] = temp
    # Возвращаем список
    return list

new_nums = mix_list(nums)
print(new_nums)


# 2 вар. с shuffle
# n = int(input('Введите количество элементов массива: '))
# nums=list(range(n))
# print(nums)
# random.shuffle(nums)
# print(nums)


