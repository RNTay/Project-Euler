#!/usr/bin/env python3

factor_list = [i for i in range(1, 21)]
x = 0
found = False


def check(n):
    global factor_list
    for a in factor_list:
        if n % a != 0:
            return False
    return True


while not found:
    x += 2*3*5*7*11*13*17*19
    found = check(x)

print(x)
