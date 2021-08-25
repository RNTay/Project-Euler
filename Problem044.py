#!/usr/bin/env python3

def pentagon_sum_and_difference(a, b):
    w_sum = 3 * (a ** 2 + b ** 2) - a - b
    sqrt_w_sum = (12 * w_sum + 1) ** 0.5
    if int(sqrt_w_sum) == sqrt_w_sum:
        if (sqrt_w_sum + 1) % 6 == 0:
            w_diff = 3 * (a ** 2 - b ** 2) - a + b
            if w_diff > 0:
                sqrt_w_diff = (12 * w_diff + 1) ** 0.5
                if int(sqrt_w_diff) == sqrt_w_diff:
                    if (sqrt_w_diff + 1) % 6 == 0:
                        # return (sqrt_w_sum + 1) // 6, (sqrt_w_diff + 1) // 6
                        return True
    # return -1, -1
    return False


loop = True
x = 1
while loop:
    for y in range(1, x + 1):
        if pentagon_sum_and_difference(x, y):
            print(x*(3*x - 1)//2 - y*(3*y - 1)//2)
            loop = False
            break
    x += 1


