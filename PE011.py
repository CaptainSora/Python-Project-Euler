from math import sqrt
from _int_tools import product


def grid_product(length):
    """
    Returns the largest product of length consecutive numbers in any cardinal
    or ordinal direction within the square grid, excluding wraparounds.
    """
    with open('p011_grid.txt') as f:
        grid = list(map(int, f.read().split()))
    maxprod = 1
    size = int(sqrt(len(grid)))
    for i in range(len(grid)):
        prodlist = [maxprod]
        # Checks to the right, bottom left, below, and bottom right in order
        if i % size <= size - length:
            prodlist += [product(grid[i:i + length])]
        if i <= size * (size - length + 1) and i % 20 >= length - 1:
            prodlist += [product(grid[i:i + (length * (size - 1)):size - 1])]
        if i <= size * (size - length + 1):
            prodlist += [product(grid[i:i + (length * size):size])]
        if i <= size * (size - length + 1) and i % 20 >= length - 1:
            prodlist += [product(grid[i:i + (length * (size + 1)):size + 1])]
        maxprod = max(prodlist)
    return maxprod


def solve(vol=0):
    return grid_product(4)
