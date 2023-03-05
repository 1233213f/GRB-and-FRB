from scipy import integrate
import numpy as np
import math

def tp(ap, bt, Ep, z, P):

    # 确定分子积分范围
    a = 1 / (1 + z)
    b = 10000 / (1 + z)

    # 确定分母积分范围
    Emin = 15
    Emax = 150

    # 计算分段点
    zz = (ap-bt)*Ep/(2+ap)

    # 定义分段函数
    def ft1(x):
        return x*((x/100)**ap)*np.exp(-(2+ap)*x/Ep)
    def fd1(x):
        return ((x/100)**ap)*np.exp(-(2+ap)*x/Ep)
    def ft2(x):
        return x*(((ap-bt)*Ep/((2+ap)*100))**(ap-bt))*np.exp(bt-ap)*(x/100)**bt
    def fd2(x):
        return (((ap-bt)*Ep/((2+ap)*100))**(ap-bt))*np.exp(bt-ap)*(x/100)**bt

    # 判断分段函数的分段区间，并进行计算
    def top():
        if zz >= Emin and zz <= Emax:
            b1, err11 = integrate.quad(ft1, a, zz)
            c, err12 = integrate.quad(ft2, zz, b)
            e, err21 = integrate.quad(fd1, Emin, zz)
            f, err22 = integrate.quad(fd2, zz, Emax)
            return b1/e + c/f
        elif zz > Emax:
            b1, err11 = integrate.quad(ft1, a, b)
            e, err21 = integrate.quad(fd1, Emin, Emax)
            return b1/e
        elif zz < Emin:
            c, err12 = integrate.quad(ft2, a, b)
            f, err22 = integrate.quad(fd2, Emin, Emax)

    # 1.602 177 33×10**(-16)J， 计算 Pbolo
    Pbolo = 1.60217733 * 10**(-9) * P * top()

    return Pbolo

# 计算光度
h = 4*math.pi*tp(-0.10444,-2.2,48.5224,2,1.9)*(4.9241E+28)**2

print(h, tp(-0.10444, -2.2, 48.5224,2 , 1.9))

-0.10444,-2.2,48.5224,2

