#!/usr/bin/env python3

# Primality test code taken from Wikipedia
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
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


nums = 3  # skip 2 to allow for +=2 instead of += 1
index = 1
last_prime = 0
while index < 10001:
    if is_prime(nums):
        last_prime = nums
        index += 1
    nums += 2
print(last_prime)
