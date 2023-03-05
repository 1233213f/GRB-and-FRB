from sympy import *
import math

def jf(ap, bt, Ep, z, P):

    a = 1 / (1 + z)
    b = 10000 / (1 + z)
    n = 10000
    dx1  = (b-a)/n
    dx2 = 135/n
    sum1 = 0
    sum2 = 0
    for i in range(0, n):
        # if (dx1*(i+1)+a) <= (ap-bt)*Ep/(2+ap):
        #     sum1 = sum1 + (dx1 * (i + 1) + a) * (((dx1 * (i + 1) + a) / 100) ** ap) * exp(-(2 + ap) * (dx1 * (i + 1) + a) / Ep)
        #     sum2 = sum2 + (((dx2 * (i + 1) + a) / 100) ** ap) * exp(-(2 + ap) * (dx2 * (i + 1) + a) / Ep)
        # else:
        # 3.2312877438522737e+67
        sum1 = sum1 + (dx1 * (i + 1) + a) * (((ap - bt) * Ep / ((2 + ap) * 100)) ** (ap - bt)) * exp((bt - ap) * ((dx1 * (i + 1) + a) / 100))**bt
        # sum2 = sum2 + (((ap - bt) * Ep / ((2 + ap) * 100)) ** (ap - bt)) * exp((bt - ap) * ((dx2 * (i + 1/2) + 15) / 100))**bt
        # print(sum2)
        # 5913.905360978716
    # fx1 = ((E/100)**ap)*exp(-(2+ap)*E/Ep)
    # fx2 = (((ap-bt)*E/((2+ap)*100))**(ap-bt))*exp((bt-ap)*(E/100))
    # fx2 = (((-0.10444 + 2.2) * 48.5224 / ((2 - 0.10444) * 100)) ^ (-0.10444 + 2.2)) * exp((-2.2 + 0.10444) * (x / 100))^(-2.2)
    # Pbolo = P * sum1 / sum2
    return sum1*dx1


h = jf(-0.10444, -2.2, 48.5224, 2, 7)
print(h)

