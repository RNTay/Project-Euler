#!/usr/bin/env python3

def number_to_words(n: int) -> str:
    if 1 <= n <= 9:
        ones_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ones_words = 'one two three four five six seven eight nine'.split()
        return ones_words[ones_nums.index(n)]
    elif 11 <= n <= 19:
        teen_nums = [11, 12, 13, 14, 15, 16, 17, 18, 19]
        teen_words = 'eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty'.split()
        return teen_words[teen_nums.index(n)]
    elif len(str(n)) == 2 and n % 10 == 0:
        tens_nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        tens_words = 'ten twenty thirty forty fifty sixty seventy eighty ninety'.split()
        return tens_words[tens_nums.index(n)]
    elif 21 <= n <= 99:
        tens_part = (n // 10) * 10
        ones_part = n % 10
        word = ''
        word += number_to_words(tens_part) + '-'
        word += number_to_words(ones_part)
        return word
    elif len(str(n)) == 3 and n % 100 == 0:
        hundreds_nums = [100, 200, 300, 400, 500, 600, 700, 800, 900]
        hundreds_words = 'one hundred;two hundred;three hundred;four hundred;five hundred;six hundred;seven ' \
                         'hundred;eight hundred;nine hundred'.split(';')
        return hundreds_words[hundreds_nums.index(n)]
    elif 101 <= n <= 999:
        hundreds_part = (n // 100) * 100
        tens_and_ones_part = n % 100
        word = ''
        word += number_to_words(hundreds_part) + ' and '
        word += number_to_words(tens_and_ones_part)
        return word
    elif n == 1000:
        return 'one thousand'


total_letters = 0
for x in range(1, 1001):
    x_in_words = number_to_words(x)
    x_in_words = x_in_words.replace(' ', '')
    x_in_words = x_in_words.replace('-', '')
    total_letters += len(x_in_words)
print(total_letters)
