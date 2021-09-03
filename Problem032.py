#!/usr/bin/env python3

from itertools import permutations


def remaining_digits(number_string: str):
    remaining = []
    all_numbers = '123456789'
    for a in all_numbers:
        if a not in number_string:
            remaining.append(int(a))
    return remaining


def check(digits: list, target_number: int):
    num_digits = len(digits)
    for sublength in range(1, len(digits) // 2 + 1):
        for left in permutations(digits, sublength):
            right_digits = set()
            for d in digits:
                if d not in left:
                    right_digits.add(str(d))

            multiplicand_string = ''
            for left_digit in left:
                multiplicand_string += str(left_digit)
            multiplicand = int(multiplicand_string)

            if target_number % multiplicand == 0:
                multiplier = target_number // multiplicand
                multiplier_string = str(multiplier)

                if len(multiplier_string) == num_digits - sublength:
                    multiplier_set = set(multiplier_string)
                    if multiplier_set == right_digits:
                        return True

    return False


wanted_products = set()
numbers = '123456789'
for p in permutations(numbers, 4):
    product = ''
    for p_i in p:
        product += p_i
    if check(remaining_digits(product), int(product)):
        wanted_products.add(int(product))
print(sum(wanted_products))


