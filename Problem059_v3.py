#!/usr/bin/env python3

import string

with open('p059_cipher.txt', 'r') as cipher_text_file:
    cipher = cipher_text_file.readline().split(',')

common_words = ['the', 'and', 'that']

best_count = 0
best_decryption = ''

decryptions_by_letter = dict()
for letter in string.ascii_lowercase:
    this_letter_xor = ''
    for cipher_char in cipher:
        this_letter_xor += chr(int(cipher_char) ^ ord(letter))
    decryptions_by_letter[letter] = this_letter_xor

decryption_array = ['' for _ in range(len(cipher))]
for letter1 in string.ascii_lowercase:
    letter1_xor = decryptions_by_letter[letter1]
    for index1 in range(0, len(cipher), 3):
        decryption_array[index1] = letter1_xor[index1]

    for letter2 in string.ascii_lowercase:
        letter2_xor = decryptions_by_letter[letter2]
        for index2 in range(1, len(cipher), 3):
            decryption_array[index2] = letter2_xor[index2]

        for letter3 in string.ascii_lowercase:
            letter3_xor = decryptions_by_letter[letter3]
            for index3 in range(2, len(cipher), 3):
                decryption_array[index3] = letter3_xor[index3]

            decrypted = ''.join(decryption_array)
            common_words_count = 0
            for word in common_words:
                common_words_count += decrypted.count(word)
            if common_words_count > best_count:
                best_count = common_words_count
                best_decryption = decrypted

ascii_values_sum = 0
for character in best_decryption:
    ascii_values_sum += ord(character)
print(ascii_values_sum)


