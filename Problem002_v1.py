#!/usr/bin/env python3

fib_seq = [1, 2]
FourMil = 4*(10**6)
even_total = 2
while fib_seq[-1] < FourMil:
    fib_seq.append(fib_seq[-2] + fib_seq[-1])
    if fib_seq[-1] % 2 == 0:
        even_total += fib_seq[-1]
print(even_total)
