from sympy import *
import math

def jf(ap, bt, Ep, z, P):

    a = 1 / (1 + z)
    b = 10000 / (1 + z)
    n = 100000
    dx1  = (b-a)/n
    dx2 = 135/n
    sum1 = 0
    sum2 = 0
    for i in range(0, n):
        if (dx1*(i+1)+a) <= (ap-bt)*Ep/(2+ap):
            sum1 = sum1 + (dx1 * (i + 0.5) + a) * (((dx1 * (i + 0.5) + a) / 100) ** ap) * exp(-(2 + ap) * (dx1 * (i + 0.5) + a) / Ep)
            sum2 = sum2 + (((dx2 * (i + 0.5) + a) / 100) ** ap) * exp(-(2 + ap) * (dx2 * (i + 0.5) + 15) / Ep)
        else:
            sum1 = sum1 + (dx1 * (i + 0.5) + a) * (((ap - bt) * Ep / ((2 + ap) * 100)) ** (ap - bt)) * exp((bt - ap) * ((dx1 * (i + 0.5) + a) / 100))**bt
            sum2 = sum2 + (((ap - bt) * Ep / ((2 + ap) * 100)) ** (ap - bt)) * exp((bt - ap) * ((dx2 * (i + 0.5) + 15) / 100))**bt
    # fx1 = ((E/100)**ap)*exp(-(2+ap)*E/Ep)
    # fx2 = (((ap-bt)*E/((2+ap)*100))**(ap-bt))*exp((bt-ap)*(E/100))
    Pbolo = P * sum1 * dx1 / (sum2 * dx2)
    print(sum1* dx1, sum2* dx2)
    return Pbolo


h = jf(-0.10444, -2.2, 48.5224, 2, 7)
print(h)

