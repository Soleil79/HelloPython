# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# line = input()
# list_1 = [int(x.strip('.,*')) for x in line.split() if x.replace("-", "").isdigit()]
# print(f'Min: {min(list_1)}')
# print(f'Max: {max(list_1)}')

# line = input()
# list_1 = [x.strip('.,*') for x in input().split() if x.replace("-", "").isdigit()]
# print(f'Min: {min(list_1, key=int)}')
# print(f'Max: {max(list_1, key=int)}')

# list_1 = []
# for x in input().split(): # Что мы делаем
#     if x.replace("-", "").isdigit(): # фильтр
#         list_1.append(x.strip('.,*') )
# print(f'Min: {min(list_1, key=int)}')
# print(f'Max: {max(list_1, key=int)}')

def check(str_list):
    for i, num in enumerate(str_list):
        str_list[i] = num.strip('.,;:?!')
        if not str_list[i].replace("-", "").isdigit():
            return []
    return str_list


def find_max_min(nums_str: str):
    list_nums = nums_str.split()
    right_list = check(list_nums)

    if right_list:
        return min(right_list, key=int), max(right_list, key=int)
    print("The data is incorrect")
    return []


print(*find_max_min(input("Enter the numbers separated by a space: ")))