#!/usr/bin/env python3

fib_seq = [1, 1]
index = 2
while len(str(fib_seq[1])) < 1000:
    next_term = fib_seq[0] + fib_seq[1]
    fib_seq[0] = fib_seq[1]
    fib_seq[1] = next_term
    index += 1
print(index)
