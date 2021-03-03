# This file is for plotting the number of steps against tolerance for the two methods on the same plot

import numpy as np
import matplotlib.pyplot as plt

def parabola(x, a, b, c):
    return a * x ** 2 + b * x + c

def parabola_prime(x, a, b):
    return 2 * a * x + b

def f(x):
    return parabola(x, 2, -10, 12)

def f_prime(x):
    return parabola_prime(x, 2, -10)

def nsteps_f1(tol, x1, x3):
    x2 = (x1 + x3) / 2
    if f(x2) < 0:
            x1 = x2
    elif f(x2) > 0:
            x3 = x2
    nsteps = 1
    while abs(f(x2)) > tol:
        x2 = (x1 + x3) / 2
        if f(x2) < 0:
            x1 = x2
        elif f(x2) > 0:
            x3 = x2
        nsteps += 1
    return nsteps

tol_range = []
for i in np.linspace(-15.0, 10.0, 10000, endpoint = True):
    tol_range.append(10.0 ** i)

nsteps_range_2point5_1 = []
for i in tol_range:
    nsteps_range_2point5_1.append(nsteps_f1(i, 2.5, 4))

def nsteps_f2(tol, x1):
    nsteps = 0
    while abs(f(x1)) > tol:
        x1 = x1 - f(x1) / f_prime(x1)
        nsteps += 1
    return nsteps

nsteps_range_1 = []
for i in tol_range:
    nsteps_range_1.append(nsteps_f2(i, 1.0))

plt.plot(tol_range, nsteps_range_2point5_1, color = "black", label = "Bisection method")
plt.plot(tol_range, nsteps_range_1, color = "blue", label = "Newton-Raphson method")
plt.xscale("log")
plt.xlabel("Tolerance")
plt.ylabel("Steps taken")
plt.title("Efficiency of bisection and Newton-Raphson methods")
plt.axis([10 ** -15, 10, -1, 51])
plt.legend(loc = "upper right")
#plt.savefig("tolerances.pdf")
plt.show()