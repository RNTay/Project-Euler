#!/usr/bin/env python3

# Save the words.txt file, making sure all words are in a single line.

with open('words.txt', 'r') as words_file:
    words = words_file.readline()

words = words.replace('\"', '')
words = words.split(',')

letters = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')

triangle_numbers = [_*(_+1)//2 for _ in range(1, 100)]

count = 0
for word in words:
    word_value = sum([letters.index(_) for _ in word])
    if word_value in triangle_numbers:
        count += 1
print(count)
