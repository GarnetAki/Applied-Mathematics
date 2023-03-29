import matplotlib.pyplot as plt
import numpy as np

# [a, b] - отрезок, на котором исследуются функции, h - шаг дискретизации
a = 1
b = 11
h = [1.6, 0.8, 0.4, 0.2, 0.1]

def rightDifferenceDerivative(h0, key):
    
    x = np.arange(a, b+0.01, 0.01)
    x1 = np.arange(a, b, h0)
    x2 = np.arange(a, b+h0, h0)
    n = (b-a)/h0
    
    #Исследуемые функции
    function1 = np.sin(x2)/(x2+2)
    function2 = np.log(x2)*np.exp(-0.01*x2)

    #Их аналитические производные
    f1derivativeAnalytical = ((x+2)*np.cos(x)-np.sin(x))/(x**2+4*x+4)
    f2derivativeAnalytical = (100-x*np.log(x))*np.exp(-0.01*x)/(100*x)
    
    #Расчёт размера массивов для производной, вычисленной численным методом
    size = int(n)
    if size < n:
        size+=1
    f1derivativeNumeric = np.zeros(size)
    f2derivativeNumeric = np.zeros(size)

    #Вычисление численной производной по формуле правой разностной производной
    j = 0
    for i in x1:
        f1derivativeNumeric[j] = (function1[j+1]-function1[j])/h0
        f2derivativeNumeric[j] = (function2[j+1]-function2[j])/h0
        j+=1

    #Построение графиков. Синий - аналитический, оранжевый - численный 
    if (key == 1):
        plt.subplot(1, 2, 1)
        plt.grid()
        plt.plot(x, f1derivativeAnalytical, x1, f1derivativeNumeric)
        plt.subplot(1, 2, 2)
        plt.grid()
        plt.plot(x, f2derivativeAnalytical, x1, f2derivativeNumeric)
        plt.show()

    return f1derivativeNumeric, f2derivativeNumeric


#Вызов функции для каждого шага дискретизации
if __name__ == "__main__": 
    rightDifferenceDerivative(h[0], 1)
    rightDifferenceDerivative(h[1], 1)
    rightDifferenceDerivative(h[2], 1)
    rightDifferenceDerivative(h[3], 1)
    rightDifferenceDerivative(h[4], 1)