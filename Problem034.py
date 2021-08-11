#!/usr/bin/env python3

import math

sum_of_all_numbers = 0
for a in range(10, 9999999):
    sum_of_digits = 0
    for d in str(a):
        sum_of_digits += math.factorial(int(d))

    if sum_of_digits == a:
        sum_of_all_numbers += a

print(sum_of_all_numbers)


