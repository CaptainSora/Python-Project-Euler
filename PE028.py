from _sequence_tools import quadratic_series


def spiral_diagonals(size):
    """
    Returns the sum of the diagonals of a size x size integer clockwise
    spiral.
    """
    x2 = int((size - 1) / 2) + 1
    d1 = quadratic_series(a=4, b=-4, c=1, x1=1, x2=x2)
    d2 = quadratic_series(a=4, b=-6, c=3, x1=2, x2=x2)
    d3 = quadratic_series(a=4, b=-8, c=5, x1=2, x2=x2)
    d4 = quadratic_series(a=4, b=-10, c=7, x1=2, x2=x2)
    return d1 + d2 + d3 + d4


def solve(vol=0):
    return spiral_diagonals(1001)
