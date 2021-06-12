#!/usr/bin/env python3

def d(n: int) -> int:
    proper_divisors_of_n = []
    for divisor_candidate in range(1, n // 2 + 1):
        if n % divisor_candidate == 0:
            proper_divisors_of_n.append(divisor_candidate)
    return sum(proper_divisors_of_n)


numbers = [number for number in range(1, 10000)]
amicable_numbers = []

while numbers:
    a = numbers[0]
    b = d(a)
    if a != b:
        if d(b) == a:
            if b in numbers:
                amicable_numbers.append(a)
                amicable_numbers.append(b)
                numbers.remove(a)
                numbers.remove(b)
                continue
    numbers.remove(a)

print(sum(amicable_numbers))
