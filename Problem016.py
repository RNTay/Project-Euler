#!/usr/bin/env python3

x = 2**1000
sum_of_digits = 0
while x != 0:
    sum_of_digits += x % 10
    x = x // 10
print(sum_of_digits)
