#!/usr/bin/env python3

def primes_up_to(n: int) -> list:
    """Returns the list all primes [2 .. n] using
    the sieve of Eratosthenes."""
    if n <= 1:
        return []

    index_is_prime = [False, False]
    index_is_prime += [True for _ in range(2, n+1)]

    sqrt_n = n**0.5
    for i in range(2, int(sqrt_n)+1):
        if index_is_prime[i]:
            for j in range(i**2, n+1, i):
                index_is_prime[j] = False

    primes_list = []
    for p in range(n+1):
        if index_is_prime[p]:
            primes_list.append(p)

    return primes_list


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


def circular_prime(n: int) -> bool:
    # input n must be prime
    s = str(n)
    rotate_s = s[-1] + s
    rotate_s = rotate_s[:-1]
    while rotate_s != s:
        if not is_prime(int(rotate_s)):
            return False
        rotate_s = rotate_s[-1] + rotate_s
        rotate_s = rotate_s[:-1]
    return True


all_primes = primes_up_to(999_999)
count = 0
for prime in all_primes:
    if circular_prime(prime):
        count += 1
print(count)
