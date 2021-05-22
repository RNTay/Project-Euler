#!/usr/bin/env python3

# Copy the grid and paste it into a file called 'numbers-grid.txt'.

numbers_file = open('numbers-grid.txt', 'r')
numbers = numbers_file.readlines()
numbers_file.close()

grid = []

# store numbers in matrix called 'grid'
for line in numbers:
    numbers_line = [int(_) for _ in line.split()]
    grid.append(numbers_line)
len_grid = len(grid)

greatest_product = 1
adjacent_length = 4

# rows
for row_index in range(0, len_grid):
    for column_index in range(0, len_grid - adjacent_length + 1):
        product = 1
        for increment in range(adjacent_length):
            product = product * grid[row_index][column_index + increment]
        if product > greatest_product:
            greatest_product = product

# columns
for column_index in range(0, len_grid):
    for row_index in range(0, len_grid - adjacent_length + 1):
        product = 1
        for increment in range(adjacent_length):
            product = product * grid[row_index + increment][column_index]
        if product > greatest_product:
            greatest_product = product

# \ diagonals
for row_index in range(0, len_grid - adjacent_length + 1):
    for column_index in range(0, len_grid - adjacent_length + 1):
        product = 1
        for increment in range(adjacent_length):
            product = product * grid[row_index + increment][column_index + increment]
        if product > greatest_product:
            greatest_product = product

# / diagonals
for row_index in range(0, len_grid - adjacent_length + 1):
    for column_index in range(adjacent_length - 1, len_grid):
        product = 1
        for increment in range(adjacent_length):
            product = product * grid[row_index + increment][column_index - increment]
        if product > greatest_product:
            greatest_product = product

print(greatest_product)
