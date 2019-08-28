from _prime_tools import all_factors


def amicable(ceiling):
    """
    Returns the sum of all amicable numbers below ceiling.
    """
    total = 0
    for i in range(1, ceiling):
        d = all_factors(i, mode="sum")
        if d > i and i == all_factors(d, mode="sum"):
            total += i + d
    return total


def solve(vol=0):
    return amicable(10000)
