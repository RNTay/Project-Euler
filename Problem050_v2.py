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


limit = 1_000_000
primes = primes_up_to(int(limit/21) + 21)
best_prime, best_length = 0, 0

for a in range(len(primes) - 1):
    consecutive_sum = primes[a]
    sum_length = 1
    this_best_prime, this_best_length = 0, 0

    for b in range(a+1, len(primes)):
        consecutive_sum += primes[b]
        sum_length += 1

        if consecutive_sum >= limit:
            break
        elif is_prime(consecutive_sum):
            this_best_prime = consecutive_sum
            this_best_length = sum_length

    if this_best_length > best_length:
        best_length = this_best_length
        best_prime = this_best_prime

print(best_prime)


