from math import log10, ceil

"""
The number of cycles can be calculated from the cycle of remainders.
"""


def cycles(num):
    """
    Returns the length of the repetend of 1/num.
    """
    remain = [10 ** ceil(log10(num)) % num]
    while remain[-1] not in remain[:-1]:
        r = remain[-1]
        while r != 0 and r < num:
            r *= 10
        remain.append(r % num)
    if remain[-1] == 0:
        return 0
    else:
        return len(remain) - remain.index(remain[-1]) - 1


def reciprocal_cycles(ceiling):
    """
    Returns the number with the largest cycle length below ceiling.
    """
    maxcycles = 0
    num = 0
    for a in range(2, ceiling):
        c = cycles(a)
        if c > maxcycles:
            maxcycles = c
            num = a
    return num


def solve(vol=0):
    return reciprocal_cycles(1000)
