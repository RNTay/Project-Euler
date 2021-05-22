#!/usr/bin/env python3

from functools import cache


@cache
def square_digit_chain(n: int) -> int:
    """Returns either 1 or 89, after recursively
    squaring and adding digits."""
    if n in [44, 32, 13, 10, 1]:
        return 1
    elif n in [85, 89, 145, 42, 20, 4, 16, 37, 58]:
        return 89
    else:
        next_n = 0
        while n != 0:
            next_n += (n % 10)**2
            n = n // 10
        return square_digit_chain(next_n)


count89 = 0
for x in range(1, 10_000_000):
    if square_digit_chain(x) == 89:
        count89 += 1
print(count89)
