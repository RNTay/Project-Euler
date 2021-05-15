#!/usr/bin/env python3

from itertools import permutations as it_perm

string_to_permute = '0123456789'
perms = it_perm(string_to_permute, 10)  # generates permutations of the string

total = 0
for perm in perms:
    pandigital_number_str = ''.join(list(perm))  # converts the permutation to an integer

    if pandigital_number_str[0] != '0':
        if int(pandigital_number_str[1:4]) % 2 == 0:
            if int(pandigital_number_str[2:5]) % 3 == 0:
                if int(pandigital_number_str[3:6]) % 5 == 0:
                    if int(pandigital_number_str[4:7]) % 7 == 0:
                        if int(pandigital_number_str[5:8]) % 11 == 0:
                            if int(pandigital_number_str[6:9]) % 13 == 0:
                                if int(pandigital_number_str[7:]) % 17 == 0:
                                    total += int(pandigital_number_str)

print(total)
