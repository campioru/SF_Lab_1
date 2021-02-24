import numpy as np
import matplotlib.pyplot as plt


# Exercise 3


# 1.

frac = 1.44
A = 1090
p = 0.033                                                           # sets the values for e^2/4(pi)(epsilon0), A and p

def V(x):
    return A * np.exp(-x / p) - frac / x                            # defines the potential V(x)

x = np.arange(0.01, 1.001, 0.001)                                   # sets the range of x values in 0.001 increments from 0.001 to 1 inclusive

plt.plot(x, 0.0 * x, color = "black")
plt.plot(x, V(x), color = "blue", label = "$V(x)$")
plt.axis([0.0, 1.0, -10, 40])
plt.xlabel("$x$")
plt.ylabel("$V(x)$")
plt.title("Plot of $V(x)$")
plt.legend(loc = "upper right")
#plt.savefig("3.1.pdf")
plt.show()                                                          # plots V(x)

# 2.

def F(x):
    return ((A * np.exp(-x / p)) / p) - frac / (x ** 2)             # defines the force F(x) = -V'(x)

plt.plot(x, 0.0 * x, color = "black")
plt.plot(x, F(x), color = "green", label = "$F(x)$")
plt.axis([0.1, 1.0, -20, 40])
plt.xlabel("$x$")
plt.ylabel("$F(x)$")
plt.title("Plot of $F(x) = -V'(x)$")
plt.legend(loc = "upper right")
#plt.savefig("3.2.pdf")
plt.show()                                                          # plots F(x)

# 3.
def V_prime(x):
    return -F(x)
def V_double_prime(x):
    return ((A * np.exp(-x / p)) / (p ** 2)) - 2 * frac / (x ** 3)  # defines V'(x) and V''(x)

# 4.

tol = 10.0 ** -14.0
x1 = 0.25                                                           # initialises tolerance and x1

nsteps = 0
while abs(V_prime(x1)) > tol:
    x1 = x1 - V_prime(x1) / V_double_prime(x1)
    nsteps += 1                                                     # repeatedly performs the Newton-Raphson method and counts the number of steps

print()
print("Initial values x1 = 0.25, tolerance =", tol)
print("x1 =", x1)
print("V'(x1) =", V_prime(x1))
print("Steps taken =", nsteps)                                      # prints x1, V'(x1) and nsteps for x1 = 0.25 and tolerance = 10^-15