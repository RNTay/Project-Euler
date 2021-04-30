#!/usr/bin/env python3

largest = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        if a >= b:
            n = a*b
            s = str(n)
            if s == s[::-1]:
                if n > largest:
                    largest = n
print(largest)
