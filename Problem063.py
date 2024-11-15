#!/usr/bin/env python3

import math

count = 0

for x in range(1, 10):
    upper_bound_for_n = int(1 / (1 - math.log(x, 10))) + 1

    for n in range(1, upper_bound_for_n + 1):
        if len(str(x ** n)) == n:
            count += 1

print(count)
