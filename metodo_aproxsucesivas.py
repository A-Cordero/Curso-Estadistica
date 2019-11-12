#@autor:Cordero Gavilan Anthony Ariano

import numpy as np
import matplotlib.pyplot as plt
def funtion(x):
    #return x - x**3 - 4*x**2 + 10 diverge
    #return np.sqrt(((10.0/x) - 4*x)) diverge
    #return 0.5*(np.sqrt(10 - x**3))
    return -4 + 4*x - 0.5*x**2
def punto_fijo():
    
    n0  = 3
    p0  = 3.8
    fp  = funtion(p0)
    #tol = np.finfo(float).eps*10
    tol = 10**(-3)
    i   = 1
    p_parcial = []
    while i <= n0:
        p   = funtion(p0)
        print("  Error absoluto        Error relativo")
        print (i, p - p0, (p - p0)/p)
        p_parcial.append(p)
        if np.abs(p - p0) < tol:
            break
        i   = i + 1
        #fa  = funtion(p)
        p0  = p
    x = []
    for i in range(0, 3):
        x.append(i)
    plt.plot(x, p_parcial, '-o')
    plt.show()
    #if i > n0:
    #    print "error"

punto_fijo()
