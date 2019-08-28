def large_sum(ndigits):
    """
    Returns the first ndigits digits of the sum.
    """
    with open('p013_numbers.txt') as f:
        intarray = list(map(int, f.read().split()))
    return int(str(sum(intarray))[:ndigits])


def solve(vol=0):
    return large_sum(10)
