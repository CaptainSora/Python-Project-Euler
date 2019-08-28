from _int_tools import nCr


def lattice_paths(size):
    """
    Returns the number of paths from corner to opposite corner of a
    size x size grid.
    """
    return nCr(2 * size, size)


def solve(vol=0):
    return lattice_paths(20)
