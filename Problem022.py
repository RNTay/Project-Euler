#!usr/bin/env python3

# Store all names in a single line in a file called 'names.txt'.

def merge(array: list, p: int, q: int, r: int):
    """Merges two sorted sub-arrays into one sorted sub-array."""
    n1 = q - p + 1  # n1 = length of array[p..q]
    n2 = r - q  # n2 = length of array[q+1..r]
    left = [array[p+_] for _ in range(0, n1)]
    right = [array[q+_+1] for _ in range(0, n2)]
    left.append('zzz')
    right.append('zzz')
    # left = [array[p], array[p+1], ..., array[q], inf]
    # right = [array[q+1], array[q+2], ..., array[r], inf]
    i = 0
    j = 0
    for k in range(p, r+1):  # sorts array[p..r]
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1


def merge_sort(array: list, p: int, r: int):
    """Performs the merge sort algorithm recursively."""
    if p < r:
        q = (p + r) // 2  # q = midpoint of array
        merge_sort(array, p, q)  # call merge_sort on array[p..q]
        merge_sort(array, q+1, r)  # call merge_sort on array[q+1..r]
        merge(array, p, q, r)  # merge sub-arrays array[p..q] and array[q+1..r]


names_file = open('names.txt', 'r')
names = names_file.readline()
names_file.close()

names = names.replace("\"", "")
names = names.split(',')

len_names = len(names)

merge_sort(names, 0, len_names-1)

letter_and_score = dict()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for score in range(1, 27):
    letter_and_score[letters[score-1]] = score

total_name_scores = 0
for name_index in range(len_names):
    name = names[name_index]
    name_score = 0
    for letter in name:
        name_score += letter_and_score[letter]
    name_score = name_score * (name_index + 1)
    total_name_scores += name_score
print(total_name_scores)
