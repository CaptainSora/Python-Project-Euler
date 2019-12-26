from itertools import count
from _pandigital_tools import is_pandigital


def pandigital_concatenation(num):
    """
    Returns the concatenated product of num and (1, ..., n) if it is pandigital
    or 0 otherwise.
    Requires n > 1, or that num < 10000
    """
    numstr = ''
    for a in count(1):
        numstr += str(num * a)
        if len(numstr) >= 9:
            break
    if len(numstr) == 9 and is_pandigital([numstr]):
        return int(numstr)
    return 0


def largest_pandigital_multiple():
    """
    Returns the largest 1-9 pandigital number that is a concatenated product.
    """
    return max([pandigital_concatenation(x) for x in range(1, 10000)])


def solve(vol=0):
    return largest_pandigital_multiple()
