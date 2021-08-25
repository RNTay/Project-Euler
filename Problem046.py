#!/usr/bin/env python3

primes = [2]

odd_number = 3
while True:
    # check if odd_number is prime
    is_prime = True
    for p in primes:
        if odd_number % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(odd_number)
        odd_number += 2
        continue

    # code only reaches here if odd_number is composite

    conjecture_true = False
    for p in primes:
        # conjecture is
        # odd_number = prime + 2*(n^2) where n is an integer
        # => n = sqrt((odd_number - prime)/2)
        n = ((odd_number - p)/2)**0.5
        if int(n) == n:  # n is a perfect square
            conjecture_true = True
            break

    if not conjecture_true:
        print(odd_number)
        break

    odd_number += 2


