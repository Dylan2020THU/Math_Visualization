# the orthogonality of trigonometric function
# 2021-3-24
# TBSI
# ZHX

import matplotlib.pyplot as plt
import numpy as np


def sinnx_cosmx(n, m):
    x = np.linspace(0, 2 * np.pi)
    y_sinnx = np.sin(n * x)
    y_cosnx = np.cos(m * x)
    y_sincos = y_sinnx * y_cosnx

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.plot(x, 0 * x, color='black')
    ax1.plot(x, y_sinnx, label='sin(%dx)' % n, color='r')
    ax1.plot(x, y_cosnx, label='cos(%dx)' % m, color='b')
    ax1.plot(x, y_sincos, label='sin(%dx)*cos(%dx)' % (n, m), color='green')

    plt.legend()
    # plt.show()


def sinnx_sinmx(n, m):
    x = np.linspace(0, 2 * np.pi)
    y_sinnx = np.sin(n * x)
    y_sinmx = np.sin(m * x)
    y_sinsin = y_sinnx * y_sinmx

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.plot(x, 0 * x, color='black')
    ax1.plot(x, y_sinnx, label='sin(%dx)' % n, color='r')
    ax1.plot(x, y_sinmx, label='sin(%dx)' % m, color='b')
    ax1.plot(x, y_sinsin, label='sin(%dx)*sin(%dx)' % (n, m), color='green')

    plt.legend()
    # plt.show()


def cosnx_cosmx(n, m):
    x = np.linspace(0, 2 * np.pi)
    y_cosnx = np.cos(n * x)
    y_cosmx = np.cos(m * x)
    y_coscos = y_cosnx * y_cosmx

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.plot(x, 0 * x, color='black')
    ax1.plot(x, y_cosnx, label='cos(%dx)' % n, color='r')
    ax1.plot(x, y_cosmx, label='cos(%dx)' % m, color='b')
    ax1.plot(x, y_coscos, label='cos(%dx)*cos(%dx)' % (n, m), color='green')

    plt.legend()
    # plt.show()


if __name__ == '__main__':
    sinnx_cosmx(1, 2)
    sinnx_sinmx(1, 2)
    cosnx_cosmx(1, 2)
    plt.show()
