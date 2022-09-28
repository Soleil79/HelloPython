# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input('Введите число, задающее размер списка: '))
numbers = [] 

for i in range(n):
    numbers.append(int((1 + 1/n) ** n))
print(numbers)
sum=0
for i in numbers:
    sum += i
print('Сумма элементов массива =', sum)




