import matplotlib.pyplot as plt
import numpy as np
from rightRectangleAntiderivative import rightRectangleAntiderivative
from leftRectangleAntiderivative import leftRectangleAntiderivative
from centerRectangleAntiderivative import centerRectangleAntiderivative
from trapezoidAntiderivative import trapezoidAntiderivative
from SimpsonAntiderivative import SimpsonAntiderivative

a = 1
b = 5
h = [0.08, 0.04, 0.02, 0.01, 0.005]
ind = [0, 1, 2, 3, 4]

#Массив аналитического интеграла для отрезков длины h0 первой функции
def f1adAnalytical(h0):
    x = np.arange(a, b+h0, h0)
    F1 = (np.sin(x**3)-(x**3)*np.cos(x**3))/3
    F = np.zeros(len(x)-1)
    j=0
    for i in F:
        F[j] = F1[j+1]-F1[j]
        j+=1
    return F

#Массив аналитического интеграла для отрезков длины h0 второй функции
def f2adAnalytical(h0):
    x = np.arange(a, b+h0, h0)
    F1 = 2*np.exp(np.sqrt(np.sinh(x)))
    F = np.zeros(len(x)-1)
    j=0
    for i in F:
        F[j] = F1[j+1]-F1[j]
        j+=1
    return F
    
#Вычисление отклонения
def standartDeviationButY1AndY2AreNumbersNotArrays(y1, y2):
    return np.sqrt(np.mean(np.power(y1 - y2, 2)))


#Построение отклонения для интегралов первой функции
plt.subplot(1, 2, 1)
plt.xlabel("h")
plt.ylabel("Отклонение")
plt.title("Отклонение F1 от h")
plt.plot(h, [standartDeviationButY1AndY2AreNumbersNotArrays(np.sum(rightRectangleAntiderivative(h[i], 0)[0]), np.sum(f1adAnalytical(h[i]))) for i in ind], label="right rectangle")
plt.plot(h, [standartDeviationButY1AndY2AreNumbersNotArrays(np.sum(leftRectangleAntiderivative(h[i], 0)[0]), np.sum(f1adAnalytical(h[i]))) for i in ind], label="left rectangle")
plt.plot(h, [standartDeviationButY1AndY2AreNumbersNotArrays(np.sum(centerRectangleAntiderivative(h[i], 0)[0]), np.sum(f1adAnalytical(h[i]))) for i in ind], label="center rectangle")
plt.plot(h, [standartDeviationButY1AndY2AreNumbersNotArrays(np.sum(trapezoidAntiderivative(h[i], 0)[0]), np.sum(f1adAnalytical(h[i]))) for i in ind], label="trapezoid")
plt.plot(h, [standartDeviationButY1AndY2AreNumbersNotArrays(np.sum(SimpsonAntiderivative(h[i], 0)[0]), np.sum(f1adAnalytical(h[i]))) for i in ind], label="Simpson")
plt.grid()
plt.legend()

#Построение отклонения для интегралов второй функции
plt.subplot(1, 2, 2)
plt.xlabel("h")
plt.ylabel("Отклонение")
plt.title("Отклонение F2 от h")
plt.plot(h, [standartDeviationButY1AndY2AreNumbersNotArrays(np.sum(rightRectangleAntiderivative(h[i], 0)[1]), np.sum(f2adAnalytical(h[i]))) for i in ind], label="right rectangle")
plt.plot(h, [standartDeviationButY1AndY2AreNumbersNotArrays(np.sum(leftRectangleAntiderivative(h[i], 0)[1]), np.sum(f2adAnalytical(h[i]))) for i in ind], label="left rectangle")
plt.plot(h, [standartDeviationButY1AndY2AreNumbersNotArrays(np.sum(centerRectangleAntiderivative(h[i], 0)[1]), np.sum(f2adAnalytical(h[i]))) for i in ind], label="center rectangle")
plt.plot(h, [standartDeviationButY1AndY2AreNumbersNotArrays(np.sum(trapezoidAntiderivative(h[i], 0)[1]), np.sum(f2adAnalytical(h[i]))) for i in ind], label="trapezoid")
plt.plot(h, [standartDeviationButY1AndY2AreNumbersNotArrays(np.sum(SimpsonAntiderivative(h[i], 0)[1]), np.sum(f2adAnalytical(h[i]))) for i in ind], label="Simpson")
plt.grid()
plt.legend()

plt.show()