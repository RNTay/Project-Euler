#!/usr/bin/env python3

def sum_is_pentagon(j, k):
    w = 3 * (j ** 2 + k ** 2) - j - k
    sqrt = (12 * w + 1) ** 0.5
    if sqrt == int(sqrt):
        if (int(sqrt) + 1) % 6 == 0:
            return True
    return False


n = 1
D = n*(3*n - 1) // 2

go_next = True
while go_next:
    tried_A = set()
    for A in range(1, int(D**0.5) + 1):
        for i in range(1, 3):  # i = 1, 2
            a = A / i
            b = D / a
            if b == int(b):
                tried_A.add(A)
                x = (2*a + 3*b + 1) / 6
                y = x - b

                if (x == int(x)) and (y > 0):
                    x = int(x)
                    y = int(y)

                    if sum_is_pentagon(x, y):
                        print(D, x, y)
                        go_next = False
                        break
    for b in tried_A:
        for i in range(1, 3):  # i = 1, 2
            a = (D / b) / i
            b *= i

            x = (2*a + 3*b + 1) / 6
            y = x - b

            if (x == int(x)) and (y > 0):
                x = int(x)
                y = int(y)

                if sum_is_pentagon(x, y):
                    print(D)
                    go_next = False
                    break

    n += 1
    D = n*(3*n - 1) // 2


