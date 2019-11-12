#metodo de newton raphso
#@autor: Cordero Gavilan Anthony
import numpy as np
import matplotlib.pyplot as plt

def funtion_real(x):
    #funcion a evaluar
    #fx = x*np.sin(x) - 1
    #fx = x**3 + 4*x**2 - 10
    #fx  = x**3 - np.sin(x)
    #fx = x**2 -2*x +1
    #fx = x**2 - 5
    #fx  = x + np.e**(-50*x**2)*np.cos(x)
    fx = x**2 - 2*x  + 0.5
    return fx

def funtion_derive(x):
    #fdx = 3*x**2 - np.cos(x)
    fdx = 2*x - 2 
    return fdx

def newton():
    seed    = 1
    #primer valor de las iteracion
    x       = 10.0
    x_n     = 0
    tol     = np.finfo(float).eps*10
    ite     = 0
    while( seed > tol):
        ite     = ite + 1
        x_n     = x - funtion_real(x)/funtion_derive(x)
        print (ite, x, seed)
        seed    = np.abs(x_n - x)/np.abs(x_n) 
        x       = x_n
x = []
y = []
for i in range( -40, 40):
    x.append(funtion_real(i))
    y.append(i)
plt.plot(y, x, '-o')
plt.show() 
newton()
