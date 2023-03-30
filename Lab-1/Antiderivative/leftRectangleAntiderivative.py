import matplotlib.pyplot as plt
import numpy as np

# [a, b] - отрезок, на котором исследуются функции, h - шаг дискретизации
a = 1
b = 5
h = [0.08, 0.04, 0.02, 0.01, 0.005]

def leftRectangleAntiderivative(h0, key):

    x = np.arange(a+h0, b+h0, h0)
    n = (b-a)/h0
    
    #Исследуемые функции
    function1 = np.sin(x**3)*(x**5)
    function2 = np.exp(np.sqrt(np.sinh(x)))*np.cosh(x)/np.sqrt(np.sinh(x))
    
    #Их аналитические интегралы
    f1antiderivativeAnalytical = -33.1271743853859
    f2antiderivativeAnalytical = 11011.97807860342

    #Вычисление численного интеграла по формуле левых прямоугольников
    f1antiderivativeNumeric = np.zeros(len(x))
    f2antiderivativeNumeric = np.zeros(len(x))

    j = 0
    for i in x:
        f1antiderivativeNumeric[j] = function1[j]*h0
        f2antiderivativeNumeric[j] = function2[j]*h0
        j+=1
    
    if key == 1:
        print([np.sum(f1antiderivativeNumeric), np.sum(f2antiderivativeNumeric)])

    return f1antiderivativeNumeric, f2antiderivativeNumeric


#Вызов функции для каждого шага дискретизации
if __name__ == "__main__": 
    leftRectangleAntiderivative(h[0], 1)
    leftRectangleAntiderivative(h[1], 1)
    leftRectangleAntiderivative(h[2], 1)
    leftRectangleAntiderivative(h[3], 1)
    leftRectangleAntiderivative(h[4], 1)