# ASP HW4 (4.3) Linear Approximation Optional
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
        b[i] = sympy.integrate((4*(t-0.5) * v[i]), (t, 0, 1))

a = np.mat(G).I * b

print('G:', G)
print('b:', b)
print('a:', a)

tt = np.linspace(0, 1)

w_t = 16*(tt-0.5)**2

x = np.exp(tt)
x_Taylor = 1 + tt + 0.5 * tt ** 2
x_hat = float(a[0])-1.012 + (float(a[1])+0.851) * tt + (float(a[2])+0.839) * (tt ** 2)



fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set(xlabel='t', ylabel='f(t)')

ax1.plot(tt, w_t, label='w(t)',c='red')
ax1.plot(tt, x, label='x(t)',c='blue')
ax1.plot(tt, x_Taylor, label='x_Taylor(t)',c='orange')
ax1.plot(tt, x_hat, label='x_hat(t)',c='green')

plt.legend()
plt.show()
