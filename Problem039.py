#!/usr/bin/env python3

def find_lengths(perimeter: int) -> list[set]:
    store_solutions = []
    for a in range(1, perimeter):
        for b in range(1, perimeter - a):
            c = (a**2 + b**2)**0.5
            if c == int(c):
                c = int(c)
                this_perimeter = a + b + c
                if this_perimeter == perimeter:
                    if {a, b, c} not in store_solutions:
                        store_solutions.append({a, b, c})
    return store_solutions


max_number_of_solutions = 0
p_for_max = 0
for p in range(2, 1001, 2):
    solutions = find_lengths(p)
    number_of_solutions = len(solutions)
    if number_of_solutions > max_number_of_solutions:
        max_number_of_solutions = number_of_solutions
        p_for_max = p

print(p_for_max)
