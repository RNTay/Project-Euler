#!/usr/bin/env python3

t = 286
p = 165
h = 143
while True:
    T = t*(t+1)//2
    P = p*(3*p-1)//2
    H = h*(2*h-1)

    if T == P == H:
        print(T)
        break

    if (T <= P) and (T <= H):
        t += 1
    elif (P <= T) and (P <= H):
        p += 1
    else:  # (H <= T) and (H <= P):
        h += 1
