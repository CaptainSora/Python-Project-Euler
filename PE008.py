from _int_tools import int_to_digit_array, product


def largest_product(adj):
    """
    Returns the greatest product of adj adjacent digits.
    """
    with open('p008_number.txt') as f:
        numarray = int_to_digit_array(f.read())
    maxsum = 0
    for i in range(len(numarray) - adj):
        maxsum = max(maxsum, product(numarray[i:i+adj]))
    return maxsum


def solve(vol=0):
    return largest_product(13)
