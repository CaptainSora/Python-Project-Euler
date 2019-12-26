from _pandigital_tools import generate


def substring_div():
    """
    Returns the sum of all 0-9 pandigital numbers with substring divisibility
    as defined in the question.
    """
    primes = [2, 3, 5, 7, 11, 13, 17]
    return len(
        [a for a in generate(0, 9)
            if all(
                [int(str(a)[b+1:b+4]) % primes[b] == 0
                    for b in range(len(primes))]
            )]
    )


def solve(vol=0):
    return substring_div()
