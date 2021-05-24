#!/usr/bin/env python3

coins = [200, 100, 50, 20, 10, 5, 2, 1]
number_of_ways = 0


def extend(our_coins: list, goal: int):
    global coins
    global number_of_ways

    if sum(our_coins) == goal:
        number_of_ways += 1
        return

    if len(our_coins) == 0:
        available_coins = coins
    else:
        available_coins = coins[coins.index(our_coins[-1]):]

    for coin in available_coins:
        our_coins.append(coin)
        if sum(our_coins) <= goal:
            extend(our_coins, goal)
        our_coins.pop()


extend(our_coins=[], goal=200)
print(number_of_ways)
