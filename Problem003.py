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


x = 1
largest = 0
num = 600851475143
while x <= num:
    if is_prime(x):
        if num % x == 0:
            if x > largest:
                largest = x
                num = num // x
    x += 1
print(largest)
