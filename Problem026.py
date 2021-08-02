#!/usr/bin/env python3

def reciprocal(d: int) -> str:
    """Returns decimal representation of 1/d  (d >= 2)"""
    answer = '0.'
    r = '10'  # remainder
    seen_r_values = []
    while int(r) != 0:
        while int(r) < d:
            r += '0'
            answer += '0'

        if r in seen_r_values:
            answer += ')'
            answer_index = 2
            repeated_r = r
            r = '10'
            while True:
                while int(r) < d:
                    r += '0'
                    answer_index += 1
                if r == repeated_r:
                    break
                r = str(int(r) % d) + '0'
                answer_index += 1
            answer = answer[:answer_index] + '(' + answer[answer_index:]
            break

        answer += str(int(r) // d)
        seen_r_values.append(r)
        r = str(int(r) % d) + '0'

    return answer


longest_period = 0
n_with_longest_period = 0
for n in range(2, 1000):
    n_inverse = reciprocal(n)
    if '(' in n_inverse:
        period = n_inverse.index(')') - n_inverse.index('(') - 1
        if period > longest_period:
            longest_period = period
            n_with_longest_period = n
print(n_with_longest_period)


