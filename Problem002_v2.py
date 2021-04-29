#!/usr/bin/env python3

a, b = 1, 2
FourMil = 4*(10**6)
even_total = 2
while b < FourMil:
    c = a + b
    a = b
    b = c
    if b % 2 == 0:
        even_total += b
print(even_total)
