#!/usr/bin/env python3

# pseudocode taken from the overview:
# https://projecteuler.net/overview=031

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200


def ways(target, largest_available_coin_index):
    global coins
    if largest_available_coin_index <= 1:
        return 1
    res = 0
    while target >= 0:
        res = res + ways(target, largest_available_coin_index-1)
        target = target - coins[largest_available_coin_index-1]
    return res


print(ways(amount, len(coins)))
