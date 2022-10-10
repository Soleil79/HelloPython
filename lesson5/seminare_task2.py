# Дан список чисел. Создайте список, в который попадают числа, 
# описывающие возрастающую последовательность. Порядок элементов меять нельзя.

# in
# 8
# Out
# [10, 0, 5, 11, 6, 1, 15, 10]
# [[10, 11, 15], [0,  5, 11, 15], [5, 11 15], [11, 15], [6, 15], [1, 15]]


from random import choices


def new_list (size):
    list_of_numbers = choices(range(1, size*2), k = size)
    return list_of_numbers
n_list = new_list(10)
print(n_list)

def range_nums (new_list: list):
    my_list = []
    for i in range(len(new_list)):
        f = new_list[i]
        lis_1 = [f]
        for j in range(i + 1, len(new_list)):
            if new_list[j] > f:
                f = new_list[j]
                lis_1.append(f)
        if len(lis_1) > 1:
            my_list.append(lis_1)
    return my_list

print(range_nums(n_list))