from math import floor


def sum_of_multiples(a, b, ceiling, vol=0):
    """
    Returns the sum of all multiples of a and b below ceiling.
    """
    def sum_mult(n):
        """
        Returns the sum of all multiples of n below ceiling.
        """
        return n * (floor((ceiling-1) / n) + 1) * (floor((ceiling-1) / n) / 2)

    return int(sum_mult(a) + sum_mult(b) - sum_mult(a * b))


def solve(vol=0):
    return sum_of_multiples(3, 5, 1000, vol=vol)
