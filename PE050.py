from _prime_tools import sieve


def consecutive_prime_sum_v2(ceiling, vol=0):
    """
    Returns the prime below ceiling which is the sum of the most consecutive
    primes.
    """
    primelist = sieve(ceiling)
    maxlen = 0
    primevalue = 0

    for a in range(len(primelist)):
        # Don't bother continuing if impossible to find longer consecutive sum
        if len(primelist) - a < maxlen:
            break
        # Start consecutive summation from primelist[a]
        for b in range(maxlen + 1, len(primelist) - a):
            # Array indexing assertion
            primesum = sum(primelist[a:a+b+1])
            if primesum > ceiling:
                break
            elif primesum in primelist:
                maxlen = b
                primevalue = primesum
    if vol >= 1:
        print(f"{primevalue} is a sum of {maxlen} consecutive primes.")
    return primevalue


def solve(vol=0):
    return consecutive_prime_sum_v2(10**6, vol=vol)
