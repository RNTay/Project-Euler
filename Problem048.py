#!/usr/bin/env python3

sum_self_powers = 0
for x in range(1, 1001):
    sum_self_powers += (x**x)
print(sum_self_powers % (10**10))
