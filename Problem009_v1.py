#!/usr/bin/env python3

for a in range(1, 1000):
    for b in range(1, 1000):
        if a < b:
            if (a**2 + b**2)**(1/2) % 1 == 0:
                for c in range(1, 1000):
                    if b < c:
                        if a**2 + b**2 == c**2:
                            if a + b + c == 1000:
                                print(a*b*c)
                                exit()
