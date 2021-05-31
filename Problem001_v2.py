#!/usr/bin/env python3

import itertools as it

multiples = [3, 5]  # all multiples should have GCD 1
below = 1000

total = 0

multiples_intersections = []
for intersection_length in range(1, len(multiples)+1):
    multiples_intersections += [list(_) for _ in it.combinations(multiples, intersection_length)]

for m_i in multiples_intersections:
    num_multiples = len(m_i)
    m = 1
    for _ in m_i:
        m = m * _
    n = (below - 1) // m
    total = total + ((-1)**(num_multiples + 1)) * n * (2*m + (n - 1)*m) // 2

print(total)
