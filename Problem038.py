#!/usr/bin/env python3

def concatenated_multiples(integer: int, m: int) -> str:
    answer = ''
    for multiple in range(1, m + 1, 1):
        answer += str(integer * multiple)
    return answer


def is_pandigital(number: str) -> bool:
    pandigital_number_set = set('123456789')
    if (len(number) == 9) and (set(number) == pandigital_number_set):
        return True
    else:
        return False


largest_pandigital = 0
Z = 1
n = 2
while int(str(Z) + str(Z*2)) <= 987654321:
    n = 2
    concat_mult = concatenated_multiples(Z, n)
    while len(concat_mult) <= 9:
        if is_pandigital(concat_mult):
            if int(concat_mult) > largest_pandigital:
                largest_pandigital = int(concat_mult)
        n += 1
        concat_mult = concatenated_multiples(Z, n)
    Z += 1

print(largest_pandigital)


