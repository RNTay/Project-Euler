#!/usr/bin/env python3

from functools import cache


@cache
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


@cache
def prime_factorisation(n: int) -> list[tuple]:
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
        return prime_factors + prime_factorisation(n)
    if n % 3 == 0:
        prime, repeat = (3, 1)
        n = n // 3
        while n % 3 == 0:
            (prime, repeat) = (prime, repeat + 1)
            n = n // 3
        prime_factors.append((prime, repeat))
        return prime_factors + prime_factorisation(n)
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
                return prime_factors + prime_factorisation(n)
        if is_prime(p + 1):
            if n % (p + 1) == 0:
                prime, repeat = (p + 1, 1)
                n = n // (p + 1)
                while n % (p + 1) == 0:
                    (prime, repeat) = (prime, repeat + 1)
                    n = n // (p + 1)
                prime_factors.append((prime, repeat))
                return prime_factors + prime_factorisation(n)
        p += 6
    return prime_factors


def sum_proper_divisors(n: int) -> int:
    sum_divisors = 1
    prime_factors = prime_factorisation(n)
    for (p, r) in prime_factors:
        sum_divisors *= (p**(r+1) - 1)//(p - 1)
    return sum_divisors - n


abundant_numbers = []
for x in range(2, 28123 + 1):
    if sum_proper_divisors(x) > x:
        abundant_numbers.append(x)

can_use_2_abundant_nums = set()
for a in abundant_numbers:
    for b in abundant_numbers:
        can_use_2_abundant_nums.add(a + b)

sum_cannot_use_2_abundant_nums = 0
for y in range(28123 + 1):
    if y not in can_use_2_abundant_nums:
        sum_cannot_use_2_abundant_nums += y

print(sum_cannot_use_2_abundant_nums)


