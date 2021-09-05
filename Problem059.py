#!/usr/bin/env python3

import string


def decrypt(cipher_text: str, key: str):
    cipher_text_numbers = cipher_text.split(',')
    plain_text = ''
    for cipher_text_index in range(len(cipher_text_numbers)):
        key_index = cipher_text_index % len(key)
        plain_text += chr(int(cipher_text_numbers[cipher_text_index]) ^ ord(key[key_index]))
    return plain_text


with open('text-file.txt', 'r') as cipher_text_file:
    cipher = cipher_text_file.readline()

common_words = ['the', 'and', 'that', 'have', 'for', 'not', 'with']

best_count = 0
best_decryption = ''
for letter1 in string.ascii_lowercase:
    for letter2 in string.ascii_lowercase:
        for letter3 in string.ascii_lowercase:
            guess_key = letter1 + letter2 + letter3

            decrypted = decrypt(cipher, guess_key)

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


