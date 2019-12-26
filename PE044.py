from math import sqrt
from itertools import count


def pent(n):
    """
    Calculates the nth pentagonal number.
    """
    return int(n * (3 * n - 1) / 2)


def is_pent(p):
    """
    Predicate for whether p is pentagonal.
    """
    if p <= 0:
        return False
    n = int(sqrt(p * 2 / 3)) + 1
    while pent(n) > p:
        n -= 1
    return pent(n) == p


def min_diff(vol=0, prove=False):
    """
    Calculates the minimum difference of any pair of pentagonal numbers whose
    sum and differences are also pentagonal.
    """
    d = 0
    for n1 in count(2):
        if d and pent(n1) - pent(n1 - 1) > d:
            return d
        for n2 in range(1, n1):
            if d and pent(n1) - pent(n2) > d:  # Only runs if prove is True
                continue
            if is_pent(pent(n1) + pent(n2)) and is_pent(pent(n1) - pent(n2)):
                if not d or pent(n1) - pent(n2) < d:
                    d = pent(n1) - pent(n2)
                    if not prove:
                        return d
            

def min_diff_old(vol=0):
    """
    Calculates the minimum difference of any pair of pentagonal numbers whose
    sum and differences are also pentagonal.
    """
    # Equivalent to finding the smallest a such that:
    #   a, b, c, d are all pentagonal
    #   a + b = c
    #   b + c = d
    pent = [1, 5]
    index = 1
    min_diff = 0
    while True:
        for a in range(index):
            summ = pent[index] + pent[a]
            diff = pent[index] - pent[a]
            while (summ > pent[-1]):
                pent.append(int(len(pent) * (3 * len(pent) - 1) / 2))
            if summ in pent and diff in pent:
                if diff < min_diff or min_diff == 0:
                    min_diff = diff
        if 0 < min_diff:
            if vol >= 1:
                print("D is %d" % min_diff)
            return min_diff
        index += 1


def solve(vol=0):
    return min_diff(vol=vol)

solve()
