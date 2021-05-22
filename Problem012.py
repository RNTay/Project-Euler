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


def prime_factorisation(n: int) -> list:
    """Returns the prime factors of n, as a list,
    with each element of the list being a tuple of:
    (prime factor, repeated times)."""
    prime_factors = []
    if n < 2:
        return []
    if n % 2 == 0:
        prime, repeat = (2, 1)
        n = n // 2
        while n % 2 == 0:
            (prime, repeat) = (prime, repeat + 1)
            n = n // 2
        prime_factors.append((prime, repeat))
    if n % 3 == 0:
        prime, repeat = (3, 1)
        n = n // 3
        while n % 3 == 0:
            (prime, repeat) = (prime, repeat + 1)
            n = n // 3
        prime_factors.append((prime, repeat))
    p = 6
    while n != 1:
        if is_prime(p - 1):
            if n % (p - 1) == 0:
                prime, repeat = (p - 1, 1)
                n = n // (p - 1)
                while n % (p - 1) == 0:
                    (prime, repeat) = (prime, repeat + 1)
                    n = n // (p - 1)
                prime_factors.append((prime, repeat))
        if is_prime(p + 1):
            if n % (p + 1) == 0:
                prime, repeat = (p + 1, 1)
                n = n // (p + 1)
                while n % (p + 1) == 0:
                    (prime, repeat) = (prime, repeat + 1)
                    n = n // (p + 1)
                prime_factors.append((prime, repeat))
        p += 6
    return prime_factors


a = 2
triangle = a*(a+1)//2
prime_divisors = prime_factorisation(triangle)
num_divisors = 1
for (prime_divisor, repeated) in prime_divisors:
    num_divisors = num_divisors * (repeated + 1)
while num_divisors <= 500:
    a += 1
    triangle = a*(a+1)//2
    prime_divisors = prime_factorisation(triangle)
    num_divisors = 1
    for (prime_divisor, repeated) in prime_divisors:
        num_divisors = num_divisors * (repeated + 1)
print(triangle)
