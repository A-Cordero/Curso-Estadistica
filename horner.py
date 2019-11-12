#metodo de horner
#@autor : Ariano Cordero Gavilan
def horner(L, a):
    L0 = L

    for  j in range(len(L), 0, -1):
        for i in range(1, j):
            L[i] =  L[i-1]*a + L[i]

    for i in range(0, len(L)):
        for j in range(0, i):
            L[i] = L[i]*10
    return L

def ParteEntera(L):
    #1  si es negativo, -1 si es negativo
    signo1 = 1
    signo2 = 1
    parteentera = 0
    total = 0

    for i in range(0, 11):
        for j in range(0, len(L)):
              total += L[j]*(i**(len(L) - j))
        if total > 0:
            signo2 = signo1
            signo1 = 1
        else:
            signo2 = signo1
            signo1 = -1
        total = 0    
            
        if i != 0:
            if signo1*signo2 < 0: #se encontro cmbio de signo
                parteentera = i - 1
        
    return parteentera
            

    
def main():
    L0 = [ 1, 0, -7, 7]
    I  = [ 1.5, 2]
    L  = L0
    a = int((I[1] + I[0])/2)
    x = 0
    digitos = 6
    print a
    for i in range(0, digitos):
        x += a*(10**( i*(-1)))
        L = horner(L, a)
        a = ParteEntera(L)
        print L
        print a
    print x 
main()
