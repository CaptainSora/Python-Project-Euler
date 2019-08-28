from itertools import permutations
from _int_tools import int_array_to_int


def lexicographic(n):
    """
    Returns the nth permutation of the digits from 0 through 9.
    """
    return int_array_to_int(list(permutations(range(10)))[n - 1])


def solve(vol=0):
    return lexicographic(10**6)

print(solve())
