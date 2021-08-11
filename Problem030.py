#!/usr/bin/env python3

power = 5

sum_of_all_numbers = 0
for a in range(10, 999999):
    sum_of_digits = 0
    for d in str(a):
        sum_of_digits += int(d) ** power

    if sum_of_digits == a:
        sum_of_all_numbers += a

print(sum_of_all_numbers)


