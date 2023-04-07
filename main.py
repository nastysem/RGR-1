import math
import numpy as np
import matplotlib.pyplot as mplt

# Данные
a = 0
b = math.pi/2
n = int(input("Число промежутков: "))
w = (b-a)/n
xl = np.linspace(a, b - w, n)
xr = np.linspace(a + w, b, n)
xm = np.linspace(a + w/2, b - w/2, n)
random_point = np.random.uniform(a, a+w)
xrand = np.linspace(random_point, b - w + random_point, n)
nl = math.sin(b) - math.sin(a)
print("По формуле Ньютона-Лейбница: " + str(nl))


# Функция
def f(x):
    return math.cos(x)


y = np.vectorize(f)

# Интегральные суммы
def summ(x):
    return np.sum(y(x)*w)


# Рисуем левую интегральную сумму
mplt.figure(figsize=(10, 5))
mplt.subplot(1, 2, 1)
mplt.plot(xl, y(xl), 'r', markersize=10)
mplt.bar(xl, y(xl), w, alpha=0.3, align='edge', edgecolor='white')
mplt.title("left Riemann sum, N={}".format(n))
# plt.show()
mplt.savefig("left Riemann sum")
print("Левые точки: " + str(summ(xl)))


# Рисуем правую интегральную сумму
mplt.figure(figsize=(10, 5))
mplt.subplot(1, 2, 1)
mplt.plot(xr, y(xr), 'b', markersize=10)
mplt.bar(xr, y(xr), w, alpha=0.3, align='edge', edgecolor='white')
mplt.title("right Riemann sum, N={}".format(n))
# plt.show()
mplt.savefig("right Riemann sum")
print("Правые точки: " + str(summ(xr)))


# Рисуем левую интегральную сумму
mplt.figure(figsize=(10, 5))
mplt.subplot(1, 2, 1)
mplt.plot(xm, y(xm), 'cyan', markersize=10)
mplt.bar(xm, y(xm), w, alpha=0.3, align='edge', edgecolor='white')
mplt.title("middle Riemann sum, N={}".format(n))
# plt.show()
mplt.savefig("middle Riemann sum")
print("Средние точки: " + str(summ(xm)))


# Рисуем случайную интегральную сумму
mplt.figure(figsize=(10, 5))
mplt.subplot(1, 2, 1)
mplt.plot(xr, y(xrand), 'm', markersize=10)
mplt.bar(xm, y(xrand), w, alpha=0.3, align='edge', edgecolor='white')
mplt.title("random Riemann sum, N={}".format(n))
# plt.show()
mplt.savefig("random Riemann sum")
print("Случайные точки: " + str(summ(xrand)))

