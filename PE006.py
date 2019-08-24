def sum_square_diff(ceiling, vol=0):
    """
    Returns the difference between the sum of the squares and the square of
    the sum for all natural numbers up to and including ceiling.
    """
    return sum(range(ceiling+1))**2 - sum([x**2 for x in range(ceiling+1)])


def solve(vol=0):
    return sum_square_diff(100, vol=vol)
