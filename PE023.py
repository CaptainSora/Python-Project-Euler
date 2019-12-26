from itertools import compress
from _prime_tools import all_factors


def nonabundant_sums(ceiling):
    """
    Returns the sum of all positive integers below ceiling which cannot be
    written as the sum of two abundant numbers.
    """
    sumflags = [True] * ceiling
    abundant = []
    for i in range(ceiling):
        if all_factors(i, mode="sum") > i:
            abundant.append(i)
            for a in abundant:
                if i + a < ceiling:
                    sumflags[i+a] = False
    return sum(compress(range(ceiling), sumflags))


def solve(vol=0):
    return nonabundant_sums(28123)
