import math

# Вариант 2
# Метод Симпсона 3/8

def f(x):
    return (x**2) * math.cos(x)


# отрезок
a = 5
b = 7

# число отрезков
m = 10
n = 3 * m

# расстояние шага
h = (b - a) / n

# разделим отрезок на точки
x = [a]
for i in range(1, n - 1):
    x.append(a + i * h)
x.append(b)

print("a, b = {}, {}".format(a, b))
print("Точек: {}".format(n))
print("Шаг: {}".format(h))
print("X = {}".format(x))

def simpsonIntegral1(f, X):
    m = len(X) // 3
    sum = 0
    for k in range(1, m):
        iter_sum = 0
        iter_sum += f(X[3 * k - 3])
        iter_sum += 3 * f(X[3 * k - 2])
        iter_sum += 3 * f(X[3 * k - 1])
        iter_sum += f(X[3 * k])
        sum += ((3 * h) / 8) * iter_sum
    return sum

def simpsonIntegral2(f, X):
    m = len(X) // 3
    sum = f(X[0]) + f(X[3 * m - 1])
    iter_sum1 = 0
    iter_sum2 = 0
    iter_sum3 = 0
    for k in range(1, m):
        iter_sum1 += f(X[3 * k - 2])
        iter_sum2 += f(X[3 * k - 1])
        if k < m - 1:
            iter_sum3 += f(X[3 * k])

    sum += 3 * iter_sum1 + 3 * iter_sum2 + 2 * iter_sum3
    sum *= (3 * h) / 8
    return sum

print("Интеграл: {}".format(simpsonIntegral1(f, x)))
print("Интеграл: {}".format(simpsonIntegral2(f, x)))