# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. 
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099
# Формула вычисления расстояния между двумя точками A(xa, ya) и B(xb, yb) на плоскости: AB = √(xb - xa)2 + (yb - ya)2

print('Нахождение расстояния между двумя точками на плоскости')
print('введите X и Y координаты точки А ')
xa = int(input()) 
ya = int(input()) 
print('введите X и Y координаты точки B ')
xb = int(input()) 
yb = int(input()) 
dist = float(((xb-xa)**2 + (yb-ya)**2)**0.5)
print(round(dist, 3))