#!/usr/bin/env python3

def gcd(x: int, y: int) -> int:
    """
    Calculates the greatest common divisor (GCD)
    of (x, y) using the Euclidean algorithm.
    """
    if x == y:
        return x
    elif x > y:
        r = [x, y]
    else:
        r = [y, x]

    while (r[1] != 1) and (r[1] != 0):
        # gcd(x, y) = gcd(y, x mod y)
        gcd_step = r[0] % r[1]
        r[0] = r[1]
        r[1] = gcd_step
    if r[1] == 1:
        return 1
    elif r[1] == 0:
        return r[0]


non_trivial_examples = []

for a in range(10, 100):
    if a % 10 != 0:  # exclude trivial examples
        for b in range(10, 100):
            if b % 10 != 0:  # exclude trivial examples and division by 0
                if a < b:  # fraction < 1
                    fraction = a / b
                    if b % 10 != 0:
                        if a % 10 == b % 10:  # a_1 = b_1
                            if (a // 10) / (b // 10) == fraction:
                                non_trivial_examples.append((a, b))
                        elif a % 10 == b // 10:  # a_1 = b_2
                            if (a // 10) / (b % 10) == fraction:
                                non_trivial_examples.append((a, b))
                        elif a // 10 == b % 10:  # a_2 = b_1
                            if (a % 10) / (b // 10) == fraction:
                                non_trivial_examples.append((a, b))
                        elif a // 10 == b // 10:  # a_2 = b_2
                            if (a % 10) / (b % 10) == fraction:
                                non_trivial_examples.append((a, b))

product_numerator = 1
product_denominator = 1
for a, b in non_trivial_examples:
    product_numerator = product_numerator * a
    product_denominator = product_denominator * b

GCD = gcd(product_numerator, product_denominator)
while GCD != 1:
    product_numerator = product_numerator // GCD
    product_denominator = product_denominator // GCD
    GCD = gcd(product_numerator, product_denominator)

print(product_denominator)
