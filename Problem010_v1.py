#!/usr/bin/env python3


# Primality test code taken from Wikipedia
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
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


total = 2
num = 3
while num < 2*(10**6):
    if is_prime(num):
        total += num
    num += 2
print(total)
