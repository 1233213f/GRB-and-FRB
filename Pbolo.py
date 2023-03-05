from scipy import integrate
import numpy as np
import math

def jf(ap, bt, Ep, z):

    # 确定相关积分范围
    a = 1 / (1 + z)
    b = 10000 / (1 + z)
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
        return x*(((ap-bt)*Ep/((2+ap)*100))**(ap-bt))*np.exp((bt-ap)*(x/100))**bt
    def fd2(x):
        return (((ap-bt)*Ep/((2+ap)*100))**(ap-bt))*np.exp((bt-ap)*(x/100))**bt

    # 定义全局变量
    # global v11, v12, v21, v22, err11, err22, err12, err21, v1, v2, err1, err2

    # 判断分段函数的分段区间，并进行计算
    if zz >= 15 and zz <= 150:
        b, err11 = integrate.quad(ft1, a, zz)
        c, err12 = integrate.quad(ft2, zz, b)

    if zz >= a and zz <= b:
        e, err21 = integrate.quad(fd1, 15, zz)
        f, err22 = integrate.quad(fd2, zz, 150)

    # 对分段的函数进行汇总
    v1 = b + c
    err1 = max(err12, err11)
    v2 = e + f
    err2 = max(err22, err21)

    return v1, err1, v2, err2

# 调用函数
P = 3.7 * 10**(-6)  # ph/cm2/sec
Dl = 2508.979475  # DL(Mpc) 1mpc=308568×100000000000×1000000=30856800000000000000000（米）

h = jf(-1.54, -2.5, 155, 0.695)
re = P * h[0]/h[2] #* 1.6 * 10**(-16)  # erg/cm2/s  1kev = 1.6*10**(-16) J  1 erg  = 10**(-7) J
Lp = 4 * math.pi * Dl**2 * re #
print(re)