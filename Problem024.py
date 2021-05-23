#!/usr/bin/env python3

import itertools as it

all_permutations = it.permutations('0123456789', 10)
count = 1
for i in all_permutations:
    if count == 1_000_000:
        print(int(''.join(list(i))))
        break
    count += 1
