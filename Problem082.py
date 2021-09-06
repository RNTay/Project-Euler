#!/usr/bin/env python3

with open('matrix.txt', 'r') as matrix_file:
    matrix = []
    for line in matrix_file.readlines():
        fixed_line = list(map(int, line.replace('\n', '').split(',')))
        matrix.append(fixed_line)

n = len(matrix)

min_paths = [[0 for _ in range(n)] for _ in range(n)]

# 1st column
for i in range(n):
    min_paths[i][0] = matrix[i][0]

# 2nd to (n-1)th column
for j in range(1, n - 1):
    # move right
    for i in range(n):
        min_paths[i][j] = min_paths[i][j - 1] + matrix[i][j]

    # check with the cell above
    for i in range(1, n, 1):
        min_paths[i][j] = min(min_paths[i][j], min_paths[i - 1][j] + matrix[i][j])

    # check with the cell below
    for i in range(n - 2, -1, -1):
        min_paths[i][j] = min(min_paths[i][j], min_paths[i + 1][j] + matrix[i][j])

# last column
for i in range(n):
    min_paths[i][-1] = min_paths[i][-2] + matrix[i][-1]

# find minimal number in last column
min_path_sum = min_paths[0][-1]
for i in range(1, n):
    if min_paths[i][-1] < min_path_sum:
        min_path_sum = min_paths[i][-1]
print(min_path_sum)


