#!/usr/bin/env python3

# Save the numbers in text_file.txt, line by line,
# ending the file with a newline.

digits_file = open('text_file.txt', 'r')
digits_line = digits_file.readline()
digits_string = ''
while len(digits_line) > 0:
    digits_string += digits_line[:-1]
    digits_line = digits_file.readline()
digits_file.close()

greatest_product = 0
for a in range(0, 1000-13):
    thirteen_string = digits_string[a:a+13]
    product = 1
    for i in thirteen_string:
        product = product * int(i)
    if product > greatest_product:
        greatest_product = product
print(greatest_product)
