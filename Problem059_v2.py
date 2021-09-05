#!/usr/bin/env python3

import string

with open('text-file.txt', 'r') as cipher_text_file:
    cipher = cipher_text_file.readline().split(',')

common_words = ['the', 'and', 'that', 'have', 'for', 'not', 'with']

best_count = 0
best_decryption = ''

decryption_array = ['' for _ in range(len(cipher))]
for letter1 in string.ascii_lowercase:
    for index1 in range(0, len(cipher), 3):
        decryption_array[index1] = chr(int(cipher[index1]) ^ ord(letter1))

    for letter2 in string.ascii_lowercase:
        for index2 in range(1, len(cipher), 3):
            decryption_array[index2] = chr(int(cipher[index2]) ^ ord(letter2))

        for letter3 in string.ascii_lowercase:
            for index3 in range(2, len(cipher), 3):
                decryption_array[index3] = chr(int(cipher[index3]) ^ ord(letter3))
            
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


