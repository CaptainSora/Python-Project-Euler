from _sequence_tools import Collatz


def longest_collatz(ceiling):
    """
    Returns the number below ceiling which produces the longest chain.
    """
    num_chain = [1, 0]
    for i in range(1, ceiling):
        steps = Collatz(i)
        if steps > num_chain[1]:
            num_chain = [i, steps]
    return num_chain[0]


def solve(vol=0):
    return longest_collatz(10**6)
