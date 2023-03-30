import matplotlib.pyplot as plt
import numpy as np
from rightDifferenceDerivative import rightDifferenceDerivative
from leftDifferenceDerivative import leftDifferenceDerivative
from centerDifferenceDerivative import centerDifferenceDerivative

a = 1
b = 11
h = [1.6, 0.8, 0.4, 0.2, 0.1]
ind = [0, 1, 2, 3, 4]

#Массив аналитической производной для узлов правой разностной производной первой функции
def f1derAnalyticalR(h0):
    x = np.arange(a, b, h0)
    return ((x+2)*np.cos(x)-np.sin(x))/(x**2+4*x+4)
    
#Массив аналитической производной для узлов правой разностной производной второй функции
def f2derAnalyticalR(h0):
    x = np.arange(a, b, h0)
    return (100-x*np.log(x))*np.exp(-0.01*x)/(100*x)

#Массив аналитической производной для узлов левой разностной производной первой функции
def f1derAnalyticalL(h0):
    x = np.arange(a+h0, b+h0, h0)
    return ((x+2)*np.cos(x)-np.sin(x))/(x**2+4*x+4)
    
#Массив аналитической производной для узлов левой разностной производной второй функции
def f2derAnalyticalL(h0):
    x = np.arange(a+h0, b+h0, h0)
    return (100-x*np.log(x))*np.exp(-0.01*x)/(100*x)

#Массив аналитической производной для узлов центральной разностной производной первой функции
def f1derAnalyticalC(h0):
    x = np.arange(a, b+h0, h0)
    return ((x+2)*np.cos(x)-np.sin(x))/(x**2+4*x+4)

#Массив аналитической производной для узлов центральной разностной производной второй функции
def f2derAnalyticalC(h0):
    x = np.arange(a, b+h0, h0)
    return (100-x*np.log(x))*np.exp(-0.01*x)/(100*x)

#Вычисление среднеквадратичного отклонения
def standartDeviation(y1, y2):
    return np.sqrt(np.mean(np.power(y1 - y2, 2)))


#Построение среднеквадратичного отклонения для производной первой функции
plt.subplot(1, 2, 1)
plt.xlabel("h")
plt.ylabel("Среднеквадратичное отклонение")
plt.title("Среднеквадратичное отклонение f'1 от h")
plt.plot(h, [standartDeviation(rightDifferenceDerivative(h[i], 0)[0], f1derAnalyticalR(h[i])) for i in ind])
plt.plot(h, [standartDeviation(leftDifferenceDerivative(h[i], 0)[0], f1derAnalyticalL(h[i])) for i in ind])
plt.plot(h, [standartDeviation(centerDifferenceDerivative(h[i], 0)[0], f1derAnalyticalC(h[i])) for i in ind])
plt.grid()

#Построение среднеквадратичного отклонения для производной второй функции
plt.subplot(1, 2, 2)
plt.xlabel("h")
plt.ylabel("Среднеквадратичное отклонение")
plt.title("Среднеквадратичное отклонение f'2 от h")
plt.plot(h, [standartDeviation(rightDifferenceDerivative(h[i], 0)[1], f2derAnalyticalR(h[i])) for i in ind])
plt.plot(h, [standartDeviation(leftDifferenceDerivative(h[i], 0)[1], f2derAnalyticalL(h[i])) for i in ind])
plt.plot(h, [standartDeviation(centerDifferenceDerivative(h[i], 0)[1], f2derAnalyticalC(h[i])) for i in ind])
plt.grid()

plt.show()