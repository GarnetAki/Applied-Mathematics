import matplotlib.pyplot as plt
import numpy as np

# [a, b] - отрезок, на котором исследуются функции, h - шаг дискретизации
a = 1
b = 11
h = [1.6, 0.8, 0.4, 0.2, 0.1]

def centerDifferenceDerivative(h0, key):

    x = np.arange(a, b+0.01, 0.01)
    x1 = np.arange(a, b+h0, h0)
    n = (b-a)/h0
    
    #Метод работает при количестве узлов > 2
    if n < 3:
        return
    
    #Исследуемые функции
    function1 = np.sin(x1)/(x1+2)
    function2 = np.log(x1)*np.exp(-0.01*x1)
    
    #Их аналитические производные
    f1derivativeAnalytical = ((x+2)*np.cos(x)-np.sin(x))/(x**2+4*x+4)
    f2derivativeAnalytical = (100-x*np.log(x))*np.exp(-0.01*x)/(100*x)
    
    #Расчёт размера массивов для производной, вычисленной численным методом
    size = int(n) + 1
    if size < n + 1:
        size+=1
    f1derivativeNumeric = np.zeros(size)
    f2derivativeNumeric = np.zeros(size)

    #Вычисление численной производной по формуле центральной разностной производной

    #В крайних точках
    f1derivativeNumeric[0] = (4*function1[1]-3*function1[0]-function1[2])/(2*h0)
    f2derivativeNumeric[0] = (4*function2[1]-3*function2[0]-function2[2])/(2*h0)
    f1derivativeNumeric[size-1] = -(4*function1[size-2]-3*function1[size-1]-function1[size-3])/(2*h0)
    f2derivativeNumeric[size-1] = -(4*function2[size-2]-3*function2[size-1]-function2[size-3])/(2*h0)
    
    #В остальных точках
    j = 0
    for i in x1:
        if j >= size-1:
            break
        
        if j > 0:
            f1derivativeNumeric[j] = (function1[j+1]-function1[j-1])/(2*h0)
            f2derivativeNumeric[j] = (function2[j+1]-function2[j-1])/(2*h0)

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
    centerDifferenceDerivative(h[0], 1)
    centerDifferenceDerivative(h[1], 1)
    centerDifferenceDerivative(h[2], 1)
    centerDifferenceDerivative(h[3], 1)
    centerDifferenceDerivative(h[4], 1)