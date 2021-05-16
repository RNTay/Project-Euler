#!/usr/bin/env python3

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimisation."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def truncatable_prime(n: int) -> bool:
    if is_prime(n):
        s = str(n)
        s = s[:-1]
        while s != '':
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        s = str(n)
        s = s[1:]
        while s != '':
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    return False


count = 0
x = 11
total = 0
while count != 11:
    if truncatable_prime(x):
        count += 1
        total += x
    x += 2
print(total)
