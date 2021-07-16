#!/usr/bin/env python3

def find_lengths(p: int) -> list[set]:
    store_solutions = []
    for a in range(1, p):
        b = int((p + a*p/(a - p))/2)
        if b >= 1:
            c = int((a**2 + b**2)**0.5)
            if a + b + c == p:
                if {a, b, c} not in store_solutions:
                    store_solutions.append({a, b, c})
    return store_solutions


max_number = 0
max_p = 0
for perimeter in range(12, 1001, 2):
    this_number = len(find_lengths(perimeter))
    if this_number > max_number:
        max_number = this_number
        max_p = perimeter
print(max_p)
