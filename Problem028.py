#!/usr/bin/env python3

n = 1
sum_diagonals = 1
spiral_size = 1

while spiral_size < 1001:
    # next spiral size
    spiral_size += 2
    steps_to_corners = spiral_size - 1

    # add the 4 corners
    for _ in range(4):
        n += steps_to_corners
        sum_diagonals += n

print(sum_diagonals)


