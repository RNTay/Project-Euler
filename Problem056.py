#!/usr/bin/env python3

maximal_digit_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        digit_sum = 0
        for digit in str(a**b):
            digit_sum += int(digit)
        if digit_sum > maximal_digit_sum:
            maximal_digit_sum = digit_sum

print(maximal_digit_sum)
