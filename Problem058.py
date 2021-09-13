#!/usr/bin/env python3

def is_prime(x: int) -> bool:
    """Primality test using 6k+-1 optimisation."""
    if x <= 3:
        return x > 1
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i ** 2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


n = 1
num_diagonals = 1
num_prime_diagonals = 0
spiral_size = 1

while True:
    # next spiral size
    spiral_size += 2
    steps_to_corners = spiral_size - 1

    num_diagonals += 4
    # add the 4 corners
    for _ in range(4):
        n += steps_to_corners
        if is_prime(n):
            num_prime_diagonals += 1

    ratio = num_prime_diagonals / num_diagonals
    if ratio < 0.1:
        print(spiral_size)
        break


