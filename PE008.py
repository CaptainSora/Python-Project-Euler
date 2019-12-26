from math import prod
from _int_tools import int_to_digit_array


def largest_product(adj):
    """
    Returns the greatest product of adj adjacent digits.
    """
    with open('p008_number.txt') as f:
        numarray = int_to_digit_array(f.read())
    return max([prod(numarray[i:i+adj]) for i in range(len(numarray) - adj)])


def solve(vol=0):
    return largest_product(13)
