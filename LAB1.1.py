import numpy as np
import matplotlib.pyplot as plt
from sys import exit

def parabola(x, a, b, c):
    return a * x ** 2 + b * x + c                                                   # defines the general form of a parabola


# Exercise 1


# 1.

def f(x):
    return parabola(x, 2, -10, 12)                                                  # defines f(x) = 2x^2 - 10x + 12, with roots x = 2 and x = 3, and minimum x = 2.5

# 2.

x = np.arange(0.0, 5.1, 0.1)                                                        # sets the range of x values in 0.1 increments from 0 to 5 inclusive

plt.plot(x, f(x), color = "blue", label = "$f(x)$")
plt.plot(x, 0.0 * x, color = "black")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Plot of $f(x) = 2x^2 - 10x + 12$")
plt.axis([0.5, 4.5, -1, 5])                                                         # plots f(x)

# 3.

x1 = 2.5
x3 = 4.0                                                                            # initialises x1 and x3

if f(x1) > 0 or f(x3) < 0:
    print("Programme not run. Change x1 and x3 so that f(x1) < 0 and f(x3) > 0.")
    exit(0)
elif f(x1) == 0 and f(x3) == 0:
    print("x1 =", x1, "and x3 =", x3, "are roots.")
    exit(0)
elif f(x1) == 0:
    print("x1 =", x1, "is a root.")
    exit(0)
elif f(x3) == 0:
    print("x3 =", x3, "is a root.")
    exit(0)                                                                         # aborts the programme if incompatible x1 or x3 entered, or if x1 or x3 are already roots

# 4.

x2 = (x1 + x3) / 2                                                                  # sets x2 to the midway point of x1 and x3

# 5.

if f(x2) < 0:
    x1 = x2
elif f(x2) > 0:
    x3 = x2                                                                         # sets x1 or x3 to x2

print()
print("x_1 =", x1)
print("x3 =", x3)                                                                   # prints new x1 and x3

# 6.

plt.plot(x2, f(x2), "ro", label = "$(x_2,f(x_2))$ after 1 step")                                                           # plots (x2,f(x2)) on the graph of f(x)
plt.legend(loc = "upper")
plt.show()                                                                          # shows graph

# 7. & 9.

tol = 0.0001
nsteps = 1                                                                          # initialises tolerance and nsteps

while abs(f(x2)) > tol:
    x2 = (x1 + x3) / 2
    if f(x2) < 0:
        x1 = x2
    elif f(x2) > 0:
        x3 = x2
    nsteps += 1                                                                     # repeatedly changes x2 until f(x2) is within the tolerance, and records the number of steps taken to do so

# 8. & 9.

print()
print("Initial values x1 = 2.5, x3 = 4.0, tolerance =", tol)
print("Actual root = 3")
print("x2 =", x2)
print("f(x2) =", f(x2))
print("Steps taken =", nsteps)                                                      # prints x2, f(x2) and nsteps for x1 = 2.5, x3 = 4.0 and tolerance = 0.0001, alongside the actual root

x1 = 2.5
x3 = 1.0
x2 = False   
nsteps = 0                                                                          # sets new values for x1 and x3, clears x2 and resets nsteps to 0

if f(x1) > 0 or f(x3) < 0:
    print("Programme not run. Change $x_1$ and $x_3$ so that $f(x_1) < 0$ and $f(x_3) > 0$.")
    exit(0)
elif f(x1) == 0 and f(x3) == 0:
    print("x1 =", x1, "and x3 =", x3, "are roots.")
    exit(0)
elif f(x1) == 0:
    print("x1 =", x1, "is a root.")
    exit(0)
elif f(x3) == 0:
    print("x3 =", x3, "is a root.")
    exit(0)                                                                         # aborts the programme if incompatible x1 or x3 entered, or if x1 or x3 are already roots

while abs(f(x2)) > tol:
    x2 = (x1 + x3) / 2
    if f(x2) < 0:
        x1 = x2
    elif f(x2) > 0:
        x3 = x2
    nsteps += 1                                                                     # repeatedly changes x2 until f(x2) is within the tolerance

print()
print("Initial values x1 = 2.5, x3 = 1.0, tolerance =", tol)
print("Actual root = 2")
print("x2 =", x2)
print("f(x2) =", f(x2))
print("Steps taken =", nsteps)                                                      # prints x2, f(x2) and nsteps for x1 = 2.5, x3 = 1.0 and tolerance = 0.0001, alongside the actual root

# 10.

def nsteps_f(tol, x1, x3):
    nsteps = 0
    x2 = (x1 + x3) / 2
    while abs(f(x2)) > tol:
        x2 = (x1 + x3) / 2
        if f(x2) < 0:
            x1 = x2
        elif f(x2) > 0:
            x3 = x2
        nsteps += 1
    return nsteps                                                                   # defines a function of nsteps for f(x) in terms of tolerance, x1 and x3

tol_range = []
for i in np.linspace(-20.0, 2.0, 2300, endpoint = True):
    tol_range.append(10.0 ** i)                                                     # creates an array with values from 10^-20 to 100, with 100 points in between each order of magnitude

nsteps_range_2point5_4 = []
for i in tol_range:
    nsteps_range_2point5_4.append(nsteps_f(i, 2.5, 4))                              # creates an array of the nsteps function applied on each value in the tol_range array, for x1 = 2.5 and x3 = 4.0

plt.plot(tol_range, nsteps_range_2point5_4, color = "black")
plt.xscale("log")
plt.xlabel("Tolerance")
plt.ylabel("Steps taken")
plt.title("Plot of steps taken against tolerance for $x_1 = 2.5$ and $x_3 = 4.0$")  # plots nsteps against tolerance for x1 = 2.5 and x3 = 4.0, with 2300 points taken

plt.show()                                                                          # shows graph