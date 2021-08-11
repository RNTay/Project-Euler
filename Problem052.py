#!/usr/bin/env python3

x = 1

while True:
    six_multiples = True
    digits = sorted(list(str(x)))
    for m in range(2, 7):
        if len(str(x)) != len(str(m*x)):
            six_multiples = False
            break
        elif sorted(list(str(m*x))) != digits:
            six_multiples = False
            break
    if six_multiples:
        print(x)
        break
    else:
        x += 1


