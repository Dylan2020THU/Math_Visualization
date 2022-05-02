# Monte-Carlo method for approximating pi
# 2022-5-2
# Hengxi Zhang
# On the railway from Shenzhen to Changsha

import numpy as np
import matplotlib.pyplot as plt

def cal_pi(n):
    l = 1  # length of the square

    A1 = l ** 2  # are of the square

    xy_min = [-l, -l]
    xy_max = [l, l]
    data_square = np.random.uniform(low=xy_min, high=xy_max, size=(n, 2))

    data_circle = []
    for i in range(n):
        if data_square[i, 0] ** 2 + data_square[i, 1] ** 2 <= A1:
            data_circle.append(data_square[i])
    if len(data_square) == 0:
        pi_approx = 0
    else:
        pi_approx = 4 * len(data_circle) / len(data_square)

    return pi_approx


# print("Samples: {}, Pi: {}".format(n, pi_approx))


if __name__ == "__main__":
    n = 5000  # number of samples
    pi_step = [0]
    pi_approx_list = [0]
    for i in range(int(n / 10), n, 100):
        pi_step.append(i)
        pi_approx_list.append(cal_pi(i))

    plt.figure(dpi=100)
    # ax1 = fig.add_subplot(1, 1, 1)
    plt.xlabel('# of samples')
    plt.ylabel('Approx. of Pi')
    plt.plot(pi_step, pi_approx_list, "-r*")
    plt.grid()
    plt.show()
