#!/usr/bin/env python3

# Save the numbers in text_file.txt, line by line,
# ending the file with a newline.

numbers_file = open('text_file.txt', 'r')
number_line = numbers_file.readline()
large_sum = 0
while len(number_line) > 0:
    number = int(number_line[:-1])
    large_sum += number
    number_line = numbers_file.readline()
numbers_file.close()

print(str(large_sum)[:10])
