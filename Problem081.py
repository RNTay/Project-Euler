#!/usr/bin/env python3

with open('text-file.txt', 'r') as matrix_file:
    matrix = []
    for line in matrix_file.readlines():
        fixed_line = list(map(int, line.replace('\n', '').split(',')))
        matrix.append(fixed_line)

n = len(matrix)

min_paths = [[0 for _ in range(n)] for _ in range(n)]

# top-left corner
min_paths[0][0] = matrix[0][0]

# top row and left column
for i in range(1, n):
    min_paths[0][i] = min_paths[0][i - 1] + matrix[0][i]
    min_paths[i][0] = min_paths[i - 1][0] + matrix[i][0]

for i in range(1, n):
    for j in range(1, n):
        min_paths[i][j] = matrix[i][j] + min(min_paths[i - 1][j], min_paths[i][j - 1])

print(min_paths[n - 1][n - 1])


