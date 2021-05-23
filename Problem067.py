#!/usr/bin/env python3

# Copy and paste the triangle of numbers into a file named 'triangle.txt'.

triangle = []
with open('triangle.txt', 'r') as triangle_file:
    triangle_lines = triangle_file.readlines()

for line in triangle_lines:
    line = [int(_) for _ in line.split()]
    triangle.append(line)

for row_index in range(len(triangle)-2, -1, -1):
    new_row = []
    for i in range(len(triangle[row_index])):
        left = triangle[row_index][i] + triangle[row_index + 1][i]
        right = triangle[row_index][i] + triangle[row_index + 1][i + 1]
        if left > right:
            new_row.append(left)
        else:
            new_row.append(right)
    triangle[row_index] = new_row
    triangle.remove(triangle[-1])
print(triangle[0][0])
