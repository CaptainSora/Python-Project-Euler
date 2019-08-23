from _prime_tools import sieve, prime_factors


def consecutive(length, dpf, vol=0):
    """
    Returns the smallest of the first length consecutive integers to have dpf
    distinct prime factors.
    """
    cand = 3
    while True:
        if prime_factors(cand, mode="count") == dpf:
            len_so_far = 1
            lowest = cand
            # Count below
            temp_cand = cand - 1
            while prime_factors(temp_cand, mode="count") == dpf:
                len_so_far += 1
                lowest = temp_cand
                temp_cand -= 1
            # Count above
            temp_cand = cand + 1
            while prime_factors(temp_cand, mode="count") == dpf:
                len_so_far += 1
                temp_cand += 1
            # Check sequence length
            if len_so_far >= length:
                if vol >= 1:
                    print(f"Found chain starting with {lowest}.")
                return lowest
        cand += 4


def solve(vol=0):
    return consecutive(4, 4, vol=vol)
