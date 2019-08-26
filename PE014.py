from _int_tools import Collatz


def longest_collatz(ceiling):
    """
    Returns the number below ceiling which produces the longest chain.
    """
    maxchain = 0
    num = 1
    for i in range(1, ceiling):
        steps = Collatz(i)
        if steps > maxchain:
            maxchain = steps
            num = i
    return num


def solve(vol=0):
    return longest_collatz(10**6)
