#!/usr/bin/env python3

Champernowne_constant = ""  # fractional part of Champernowne's constant
for i in range(1, 1_000_001):
    Champernowne_constant += str(i)

product = 1
for j in range(7):
    product = product * int(Champernowne_constant[10**j - 1])

print(product)
