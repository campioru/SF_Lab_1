import numpy as np
import matplotlib.pyplot as plt

def parabola(x, a, b, c):
    return a * x ** 2 + b * x + c                                                       # defines the general form of a parabola

def parabola_prime(x, a, b):
    return 2 * a * x + b                                                                # defines the general form of the derivative of a parabola


# Exercise 2


# 1.

def f(x):
    return parabola(x, 2, -10, 12)                                                      # defines f(x) = 2x^2 - 10x + 12, with roots x = 2 and x = 3, and minimum x = 2.5
def f_prime(x):
    return parabola_prime(x, 2, -10)                                                    # defines f'(x)

x = np.arange(0.0, 5.1, 0.1)                                                            # sets the range of x values in 0.1 increments from 0 to 5 inclusive

plt.plot(x, 0.0 * x, color = "black")
plt.plot(x, f(x), color = "blue", label = "$f(x)$")
plt.plot(x, f_prime(x), color = "green", label = "$f'(x)$")
plt.axis([0.5, 4.5, -1, 5])
plt.xlabel("$x$")
plt.ylabel("$f(x), f\,'(x)$")
plt.title("Plot of $f(x)$ and $f\,'(x)$")                                               # plots f(x) and f'(x)

# 2.

x1 = 1.0                                                                                # initialises x1

# 3.

x1 = x1 - f(x1) / f_prime(x1)                                                           # performs one iteration of the Newton-Raphson method on x1

# 4.

plt.plot(x1, f(x1), "ro", label = "$(x1,f(x1))$ after 1 step")
plt.legend(loc = "upper")
#plt.savefig("2.1.pdf")
plt.show()                                                                              # plots the result after one iteration on the graph of f(x) and f'(x)

# 5. & 7.

tol = 0.0001
nsteps = 1                                                                              # initialises tolerance and nsteps

while abs(f(x1)) > tol:
    x1 = x1 - f(x1) / f_prime(x1)
    nsteps += 1                                                                         # repeatedly performs the Newton-Raphson method and counts the number of steps

# 6. & 7.

print()
print("Initial values x1 = 1.0, tolerance =", tol)
print("Actual root = 2")
print("x1 =", x1)
print("f(x1) =", f(x1))
print("Steps taken =", nsteps)                                                          # prints x1, f(x1) and nsteps for x1 = 1.0, alongside the actual root

x1 = 4.0
nsteps = 0                                                                              # initialises x1 and nsteps

while abs(f(x1)) > tol:
    x1 = x1 - f(x1) / f_prime(x1)
    nsteps += 1                                                                         # repeatedly performs the Newton-Raphson method and counts the number of steps

print()
print("Initial values x1 = 4.0, tolerance =", tol)
print("Actual root = 3")
print("x1 =", x1)
print("f(x1) =", f(x1))
print("Steps taken =", nsteps)                                                          # prints x1, f(x1) and nsteps for x1 = 4.0 and tolerance = 0.0001, alongside the actual root

# 7.

def nsteps_f(tol, x1):
    nsteps = 0
    while abs(f(x1)) > tol:
        x1 = x1 - f(x1) / f_prime(x1)
        nsteps += 1
    return nsteps                                                                       # defines a function of nsteps for f(x) in terms of tolerance and x1

tol_range = []
for i in np.linspace(-20.0, 2.0, 2300, endpoint = True):
    tol_range.append(10.0 ** i)                                                         # creates an array with values from 10^-20 to 100, with 100 points in between each order of magnitude

nsteps_range_1 = []
for i in tol_range:
    nsteps_range_1.append(nsteps_f(i, 1.0))                                             # creates an array of the nsteps function applied on each value in the tol_range array, for x1 = 1

plt.plot(tol_range, nsteps_range_1, color = "black")
plt.xscale("log")
plt.xlabel("Tolerance")
plt.ylabel("Steps taken")
plt.title("Plot of steps taken against tolerance for $x_1 = 1$")                        # plots nsteps against tolerance for x1 = 1, with 2300 points taken
#plt.savefig("2.2.pdf")
plt.show()                                                                              # shows graph

# 8.

powers = [9.0, 9.3, 9.4, 10.0, 100.0, 1000.0]
tolerance_array = []
for power in powers:
    tolerance_array.append(10.0 ** -power)                                              # sets a range of values for tolerance, used below

for root in [2.0, 3.0]:
    print()
    print("Actual root =", root)
    for tolerance in tolerance_array:
        nsteps = 0
        if root == 2.0:
            x1 = 1
        elif root == 3.0:
            x1 = 4
        while abs(f(x1)) > tolerance:
            x1 = x1 - f(x1) / f_prime(x1)
            nsteps += 1
        print("Tolerance =", tolerance, ", estimated root =", x1, ", nsteps =", nsteps) # calculates each estimated root for a range of tolerances, and prints the list of corresponding actual roots, tolerances, estimated roots and steps taken