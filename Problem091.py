#!/usr/bin/env python3

def dot_product(vector1, vector2):
    answer = 0
    for r in range(len(vector1)):
        answer += vector1[r] * vector2[r]
    return answer


limit = 50
count = 0
for x1 in range(0, limit + 1):
    for y1 in range(0, limit + 1):
        if [x1, y1] == [0, 0]:
            continue
        for x2 in range(0, limit + 1):
            for y2 in range(0, limit + 1):
                if [x2, y2] == [0, 0]:
                    continue
                OP = [x1, y1]
                OQ = [x2, y2]
                if OP == OQ:
                    continue
                PQ = [x1 - x2, y1 - y2]
                if dot_product(OP, OQ) == 0:
                    count += 1
                elif dot_product(OP, PQ) == 0:
                    count += 1
                elif dot_product(OQ, PQ) == 0:
                    count += 1
print(count // 2)


