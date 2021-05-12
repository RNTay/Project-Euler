#!/usr/bin/env python3

import math

x = math.factorial(100)
sum_of_digits = 0
while x != 0:
    sum_of_digits += x % 10
    x = x // 10
print(sum_of_digits)
