import math


def choose(n, r):
    return math.factorial(n) // (math.factorial(r)*math.factorial(n - r))


print(choose(40, 20))
