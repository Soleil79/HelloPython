from sympy import *
from sympy.plotting import plot

x = Symbol("x")

f = -18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
# f = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18
# f = (x ** 2 + 3) / (3 * (x + 1))

# f = -12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
# f = 3 * x ** 4 - 16 * x ** 3 + 24 + x ** 2 - 11
f

# 1 Определить корни
# Нули функции.

print(solveset(f, x, Reals).evalf(2))


# 2 Найти интервалы, на которых функция возрастает
# 3 Найти интервалы, на которых функция убывает

f_diff = [-oo, oo]
f_diff[1:1] = solveset(diff(f), x, Reals).evalf(2)

incr_list = []
decr_list = []

for i in range(1, len(f_diff)):
    val = is_increasing(f, Interval.open(f_diff[i - 1], f_diff[i]))
    if val:
        incr_list.append(f"[{f_diff[i - 1]}, {f_diff[i]}]")
    else:
        decr_list.append(f"[{f_diff[i - 1]}, {f_diff[i]}]")

print(f"Убывает на интервалах:", *decr_list, sep="\n")
print(f"Возрастает на интервалах:", *incr_list, sep="\n")

# 4 Построить график

# 1
plot(f, (x, -1, 1), legend=True)

# 2
# plot(f, (x, -4, 4), legend=True)

# 3
# plot(f, (x, -4, 3), ylim=(-5, 5), legend=True)

# f_1 = plot(f, (x, -5, -1.1), show=False)
# f_2 = plot(f, (x, -0.9, 5), show=False)
# f_1.append(f_2[0])
# f_1.show()

# plot(f, (x, -1, 1.2), legend=True)



# 5 Вычислить вершину
from random import uniform

f_diff = sorted(solveset(diff(f), x, Reals).evalf(2))
f_diff.insert(0, f_diff[0] - 1)
f_1 = diff(f)

ext_list = []

for i, val in enumerate(f_diff):
    ext_list.append(f_1.subs(x, uniform(val, f_diff[i] + 1)))
    if i != 0:
        if ext_list[i - 1] < 0 < ext_list[i]:
            print(f"Точка минимума: {val}, {f.subs(x, val).evalf(2)}")
        elif ext_list[i - 1] > 0 > ext_list[i]:
            print(f"Точка максимума: {val}, {f.subs(x, val).evalf(2)}")

# 6 Определить промежутки, на котором f > 0

# 7 Определить промежутки, на котором f < 0

# Промежутки постоянства

print("f > 0: ", end="")
print(solveset(f > 0, x, Reals).evalf(2))

print("f < 0: ", end="")
print(solveset(f < 0, x, Reals).evalf(2))