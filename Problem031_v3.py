#!/usr/bin/env python3

# pseudocode taken from the overview:
# https://projecteuler.net/overview=031

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
ways = [0 for _ in range(amount+1)]
ways[0] = 1
for i in range(0, 8):
    for j in range(coins[i], amount+1):
        ways[j] = ways[j] + ways[j - coins[i]]
print(ways[amount])
