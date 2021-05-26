#!/usr/bin/env python3

from functools import cache


@cache
def is_prime(p: int) -> bool:
    """Primality test using 6k+-1 optimisation."""
    if p <= 3:
        return p > 1
    if p % 2 == 0 or p % 3 == 0:
        return False
    i = 5
    while i ** 2 <= p:
        if p % i == 0 or p % (i + 2) == 0:
            return False
        i += 6
    return True


max_number = 0
max_a, max_b = 0, 0
for a in range(-999, 1000):
    # since n = 0 must give a prime,
    # b > 0 and b is prime
    for b in range(6, 1001, 6):
        if is_prime(b + 1):
            count_primes = 1
            n = 1
            while is_prime(n**2 + a*n + (b + 1)):
                n += 1
            if n > max_number:
                max_number = n
                max_a, max_b = a, (b + 1)
        if is_prime(b - 1):
            count_primes = 1
            n = 1
            while is_prime(n ** 2 + a * n + (b - 1)):
                n += 1
            if n > max_number:
                max_number = n
                max_a, max_b = a, (b - 1)
print(max_a * max_b)
