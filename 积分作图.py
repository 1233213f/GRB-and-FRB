import numpy as np
from matplotlib import pyplot as plt

# E = symbols("E")
ap = -0.10444
bt = -2.2
Ep = 48.5224
z = 2
a = 1/(1+z)
b = 10000/(1+z)
# fx1 = ((E/100)**ap)*exp(-(2+ap)*E/Ep)
# fx2 = (((ap-bt)*E/((2+ap)*100))**(ap-bt))*exp((bt-ap)*(E/100))

x = np.linspace(a-10, b+100, 10000)
y = (((-0.10444 + 2.2) * 48.5224 / ((2 - 0.10444) * 100)) ** (-0.10444 + 2.2)) * np.exp((-2.2 + 0.10444) * (x / 100))**(-2.2)

plt.axis([np.min(x), np.max(x), 0, np.max(y)])  # 坐标范围
plt.plot(x, y, label="f(E)")  # 画曲线，带图示
plt.fill_between(x, y1=y, y2=0, where=(x >= a) & (x <= b),  # 填充积分区域
                 facecolor='blue', alpha=0.2)
# plt.text(0.5 * (0.7 + 4), 0.4, r"$int_{0.7}^4(cos(2πx)e^{-x}+1.2)mathrm{d}x$",
#          horizontalalignment='center', fontsize=14)  # 增加说明文本
plt.legend()  # 显示图示
plt.show()