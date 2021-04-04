# ASP HW4 (4.3) Linear Approximation
# 2021-4-4
# TBSI
# ZHX

import sympy
import numpy as np
import matplotlib.pyplot as plt

t = sympy.symbols('t')

G = np.zeros((3, 3))
b = np.zeros((3, 1))

v = [1, t, t ** 2]

for i in range(3):
    for j in range(3):
        G[i][j] = sympy.integrate((v[j] * v[i]), (t, 0, 1))
        b[i] = sympy.integrate((sympy.exp(t) * v[i]), (t, 0, 1))

a = np.mat(G).I * b

print('G:', G)
print('b:', b)
print('a:', a)

tt = np.linspace(0, 1)
x = np.exp(tt)
x_Taylor = 1 + tt + 0.5 * tt ** 2
x_hat = float(a[0]) + float(a[1]) * tt + float(a[2]) * (tt ** 2)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set(xlabel='t', ylabel='f(t)')

ax1.plot(tt, x, label='x',linestyle='solid',c='purple')
ax1.plot(tt, x_Taylor, label='x_Tay',linestyle='dashed',c='r')
ax1.plot(tt, x_hat, label='x_hat',linestyle='dashdot',c='b')

plt.legend()
plt.show()
