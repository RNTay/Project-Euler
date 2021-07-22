#!/usr/bin/env python3
num_prime_factors = dict()


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


def num_prime_factors_is_x(n: int, x: int) -> bool:
    global num_prime_factors
    store_n = n
    npf = 0  # npf = num prime factors

    if n < 2:
        return False
    if is_prime(n):
        num_prime_factors[store_n] = 1
        return False

    if n % 2 == 0:
        npf += 1
        while n % 2 == 0:
            n = n // 2
    if n % 3 == 0:
        npf += 1
        while n % 3 == 0:
            n = n // 3

    if n in num_prime_factors:
        npf += num_prime_factors[n]
        num_prime_factors[store_n] = npf
        return npf == x

    p = 6
    while n != 1:
        if is_prime(p - 1):
            if n % (p - 1) == 0:
                npf += 1
                while n % (p - 1) == 0:
                    n = n // (p - 1)
        if is_prime(p + 1):
            if n % (p + 1) == 0:
                npf += 1
                while n % (p + 1) == 0:
                    n = n // (p + 1)

        if n in num_prime_factors:
            npf += num_prime_factors[n]
            num_prime_factors[store_n] = npf
            return npf == x

        p += 6

    num_prime_factors[store_n] = npf
    return npf == x


num_primes_wanted = 4

a, b, c, d = 1, 2, 3, 4
p_a = num_prime_factors_is_x(a, num_primes_wanted)
p_b = num_prime_factors_is_x(b, num_primes_wanted)
p_c = num_prime_factors_is_x(c, num_primes_wanted)
p_d = num_prime_factors_is_x(d, num_primes_wanted)

while True:
    if p_a and p_b and p_c and p_d:
        break

    a = b
    b = c
    c = d
    d += 1

    p_a = p_b
    p_b = p_c
    p_c = p_d
    p_d = num_prime_factors_is_x(d, num_primes_wanted)


print(a)
