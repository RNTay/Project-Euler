from functools import cache


@cache
def collatz_length(n: int) -> int:
    """Returns the length of the Collatz sequence."""
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + collatz_length(n//2)
        else:
            return 2 + collatz_length((3*n+1) // 2)


longest = 0
number_with_longest_chain = 0
for x in range(1, 1_000_000):
    this_length = collatz_length(x)
    if this_length > longest:
        longest = this_length
        number_with_longest_chain = x
print(number_with_longest_chain)
