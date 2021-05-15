#!/usr/bin/env python3

def is_palindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False


def binary(base10: int) -> int:
    base2 = ''
    while base10 != 0:
        base2 = str(base10 % 2) + base2
        base10 = base10 // 2
    return int(base2)


sum_palindromes = 0
# even numbers are not palindromes in base 2
# (in binary, they are 1..0)
for n in range(1, 1_000_000, 2):
    if is_palindrome(n):
        binary_n = binary(n)
        if is_palindrome(binary_n):
            sum_palindromes += n
print(sum_palindromes)
