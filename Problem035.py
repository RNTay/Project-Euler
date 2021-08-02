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


num_circular_primes = 2  # because the code below will exclude 2 and 5
primes_below_1_mil = primes_up_to(10**6 - 1)

for a in primes_below_1_mil:
    is_circular = True
    a = str(a)

    if any(('0' in a, '2' in a, '4' in a, '6' in a, '8' in a, '5' in a)):
        # a permutation will have an even number or 5 at the end
        continue

    original_a = a
    for _ in range(len(a) - 1):
        a = a[1:] + a[0]
        if int(a) not in primes_below_1_mil:
            is_circular = False
            break

    if is_circular:
        num_circular_primes += 1

print(num_circular_primes)


