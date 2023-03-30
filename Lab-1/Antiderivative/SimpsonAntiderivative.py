import matplotlib.pyplot as plt
import numpy as np

# [a, b] - отрезок, на котором исследуются функции, h - шаг дискретизации
a = 1
b = 5
h = [0.08, 0.04, 0.02, 0.01, 0.005]

def SimpsonAntiderivative(h0, key):
    
    x1 = np.arange(a, b+h0, h0)
    x = np.arange(a, b+h0, h0/2)
    n = (b-a)/h0
    
    #Исследуемые функции
    function1 = np.sin(x**3)*(x**5)
    function2 = np.exp(np.sqrt(np.sinh(x)))*np.cosh(x)/np.sqrt(np.sinh(x))
    
    #Их аналитические интегралы
    f1antiderivativeAnalytical = -33.1271743853859
    f2antiderivativeAnalytical = 11011.97807860342

    #Вычисление численного интеграла по формуле Симпсона
    f1antiderivativeNumeric = np.zeros(len(x1)-1)
    f2antiderivativeNumeric = np.zeros(len(x1)-1)
    
    j = 0
    for i in x1:
        if j < len(x1)-1:
            f1antiderivativeNumeric[j] = (function1[2*j]+4*function1[2*j+1]+function1[2*j+2])*h0/6
            f2antiderivativeNumeric[j] = (function2[2*j]+4*function2[2*j+1]+function2[2*j+2])*h0/6
        j+=1
    
    if key == 1:
        print([np.sum(f1antiderivativeNumeric), np.sum(f2antiderivativeNumeric)])

    return f1antiderivativeNumeric, f2antiderivativeNumeric


#Вызов функции для каждого шага дискретизации
if __name__ == "__main__": 
    SimpsonAntiderivative(h[0], 1)
    SimpsonAntiderivative(h[1], 1)
    SimpsonAntiderivative(h[2], 1)
    SimpsonAntiderivative(h[3], 1)
    SimpsonAntiderivative(h[4], 1)