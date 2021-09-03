#!/usr/bin/env python3

from math import log2

largest = 0
line_counter = 0
best_line = 0
with open('base_exp.txt', 'r') as base_exps_file:
    for line in base_exps_file:
        line_counter += 1
        base, exp = tuple(map(int, line[:-1].split(',')))
        this_base_exp = exp * log2(base)
        if this_base_exp > largest:
            largest = this_base_exp
            best_line = line_counter
print(best_line)


