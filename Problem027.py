#!/usr/bin/env python3

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
    for b in range(-999, 1001):
        count_primes = 0
        n = 0
        while is_prime(n**2 + a*n + b):
            n += 1
        if n > max_number:
            max_number = n
            max_a, max_b = a, b
print(max_a * max_b)
