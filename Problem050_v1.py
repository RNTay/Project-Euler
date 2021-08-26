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


primes = primes_up_to(999_999)
last_prime = primes[-1]
best_prime, best_length = 0, 0

for a in range(len(primes) - 1):
    print(primes[a])
    consecutive_sum = primes[a]
    sum_length = 1
    this_best_prime, this_best_length = 0, 0

    for b in range(a+1, len(primes)):
        consecutive_sum += primes[b]
        sum_length += 1

        if consecutive_sum > last_prime:
            break
        elif consecutive_sum in primes:
            this_best_prime = consecutive_sum
            this_best_length = sum_length

    if this_best_length > best_length:
        best_length = this_best_length
        best_prime = this_best_prime

print(best_prime)


