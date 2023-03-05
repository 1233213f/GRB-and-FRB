from scipy import integrate
import numpy as np
import math

ap = -1.88
bt = -2.48
Ep = 65
z = 0.443

    # 确定相关积分范围
a = 1 / (1 + z)
b = 10000 / (1 + z)
# print(a,b)
Emin = 40
Emax = 700

    # 计算分段点
zz = (ap-bt)*Ep/(2+ap)
print(zz)

    # 定义分段函数
def ft1(x):
    return x*((x/100)**ap)*np.exp(-(2+ap)*x/Ep)
def fd1(x):
    return ((x/100)**ap)*np.exp(-(2+ap)*x/Ep)
def ft2(x):
    return x*(((ap-bt)*Ep/((2+ap)*100))**(ap-bt))*np.exp(bt-ap)*(x/100)**bt
def fd2(x):
    return (((ap-bt)*Ep/((2+ap)*100))**(ap-bt))*np.exp(bt-ap)*(x/100)**bt

    # 定义全局变量
    # global v11, v12, v21, v22, err11, err22, err12, err21, v1, v2, err1, err2

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
        return c/f
print(top())

# def down():
#     if zz >= Emin and zz <= Emax:
#         e, err21 = integrate.quad(fd1, Emin, zz)
#         f, err22 = integrate.quad(fd2, zz, Emax)
#         return e + f
#     elif zz > Emax:
#         e, err21 = integrate.quad(fd1, Emin, Emax)
#         return e
#     elif zz < Emin:
#         f, err22 = integrate.quad(fd2, Emin, Emax)
#         return f
# print(down())
# 1 kev  =  1.6 * 10**(-9) erg
P = 1.3 * 10**(-6)
# 1.602 177 33×10**(-16)
Pbolo = 1.60217733*10**(-16) * P * top() * 10**7*1243794.9203946427
# ww = 6.59767*10**(-6)/Pbolo
print(Pbolo)

