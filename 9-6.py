# -*- coding:utf-8 -*-
# 数值方法解弹簧运动方程
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1.7, 0.1)
delta = 0.1
x = np.zeros(17)
v = np.zeros(17)
a = np.zeros(17)
x[0] = 1.000
v[0] = 0.000
a[0] = -1.000

for i in range(1, 17):
    v[i] = v[i-1] + a[i-1]*delta
    x[i] = x[i-1] + delta*v[i-1]
    a[i] = -1*x[i]

plt.plot(t, x, 'o')
y = np.cos(t)
plt.plot(t, y)
plt.show()