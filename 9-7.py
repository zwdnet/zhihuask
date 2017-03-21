# -*- coding:utf-8 -*-
# 行星运动方程模拟
import numpy as np
import matplotlib.pyplot as plt

def run(N):

    t = np.arange(0.0, N, 0.1)

    x = np.zeros(N*10)
    vx = np.zeros(N*10)
    ax = np.zeros(N*10)

    y = np.zeros(N*10)
    vy = np.zeros(N*10)
    ay = np.zeros(N*10)

    r = np.zeros(N*10)
    r3 = np.zeros(N*10)

    x[0] = 0.500
    vx[0] = -0.200
    ax[0] = -4.00
    y[0] = 0.000
    vy[0] = 1.630
    ay[0] = 0.000
    r[0] = 0.500
    r3[0] = 8.000

    delta = 0.00001
    for i in range(1, N*10):
        vx[i] = vx[i-1] + ax[i-1]*delta
        vy[i] = vy[i-1] + ay[i-1]*delta
        x[i] = x[i-1] + vx[i-1]*delta
        y[i] = y[i-1] + vy[i-1]*delta
        r[i] = np.sqrt(x[i]**2 + y[i]**2)
        r3[i] = 1/r[i]**3
        ax[i] = -1*x[i]*r3[i]
        ay[i] = -1*y[i]*r3[i]

    plt.title("模拟次数%d" % int(N*10))
    plt.plot(x,y)
    plt.show()

if __name__ == "__main__":
    run(300000)
