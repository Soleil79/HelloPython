# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

# in
# Enter a real number: 8.98765
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

from decimal import Decimal

def Change():
    # accuracy = input('Введите точность: ')
    list = [input('Введите точность в формате 0.0001: ')] 
    ll = len(list)
    temp = list[ll-1]
    list[ll-1] = list[0]
    list[0] = temp
    accur = Decimal(''.join(map(str, list)))
    return accur

num = Decimal(input('Введите число: '))
accuracy = Change()
num = num.quantize(Decimal(accuracy))
print(num)
