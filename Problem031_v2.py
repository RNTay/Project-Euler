#!/usr/bin/env python3

# pseudocode taken from the overview:
# https://projecteuler.net/overview=031

from functools import cache

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200


@cache
def ways(target, largest_available_coin_index):
    global coins
    if largest_available_coin_index <= 0:
        return 1
    result = 0
    while target >= 0:
        result = result + ways(target, largest_available_coin_index-1)
        target = target - coins[largest_available_coin_index]
    return result


print(ways(amount, len(coins)-1))
