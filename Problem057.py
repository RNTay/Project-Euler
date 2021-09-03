#!/usr/bin/env python3

from fractions import Fraction

sqrt2 = 2 + Fraction(1, 2)
count = 0
for _ in range(1000):
    current_sqrt2 = sqrt2 - 1
    if len(str(current_sqrt2.numerator)) > len(str(current_sqrt2.denominator)):
        count += 1
    sqrt2 = 2 + Fraction(1, sqrt2)
print(count)


