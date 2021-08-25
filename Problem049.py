def primes_up_to(n: int) -> list:
    """Returns the list all primes [2 .. n] using
    the sieve of Eratosthenes."""
    if n <= 1:
        return []

    index_is_prime = [False, False]
    index_is_prime += [True for _ in range(2, n+1)]

    sqrt_n = n**0.5
    for i in range(2, int(sqrt_n)+1):
        if index_is_prime[i]:
            for j in range(i**2, n+1, i):
                index_is_prime[j] = False

    primes_list = []
    for p in range(n+1):
        if index_is_prime[p]:
            primes_list.append(p)

    return primes_list


# 4-digit primes
primes = primes_up_to(9999)[len(primes_up_to(999)):]
answer = ''
for p_i in range(0, len(primes) - 1):
    p1 = sorted(str(primes[p_i]))
    for p_j in range(p_i + 1, len(primes) - 1):
        p2 = sorted(str(primes[p_j]))
        if p1 == p2:
            difference = primes[p_j] - primes[p_i]
            primes_p_k = primes[p_j] + difference
            p3 = sorted(str(primes_p_k))
            if p2 == p3:
                if primes_p_k in primes:
                    answer = str(primes[p_i]) + str(primes[p_j]) + str(primes_p_k)
                    if answer == '148748178147':
                        continue
                    else:
                        print(answer)
                        exit()


