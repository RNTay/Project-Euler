#!/usr/bin/env python3

from itertools import permutations as it_perm


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


largest_pandigital_prime = 0

# largest pandigital number is 9-digits long (987654321)
# we can skip 2-, 3-, 5-, 6-, 8-, and 9-digit pandigitals because
# 1+2 == 3 == 0 (mod 3)
# 1+2+3 == 6 == 0 (mod 3)
# 1+2+...+5 == 15 == 0 (mod 3)
# 1+2+...+6 == 21 == 0 (mod 3)
# 1+2+...+8 == 36 == 0 (mod 3)
# 1+2+...+9 == 45 == 0 (mod 3)
# so these are all divisible by 3.

for n_digit in [4, 7]:
    string_to_permute = ''.join([str(_) for _ in range(1, n_digit+1)])  # creates the string '12..n'
    perms = it_perm(string_to_permute, n_digit)  # generates permutations of the string
    # perms are already in ascending order

    for perm in perms:
        pandigital_number = int(''.join(list(perm)))  # converts the permutation to an integer
        if is_prime(pandigital_number):
            largest_pandigital_prime = pandigital_number

print(largest_pandigital_prime)
