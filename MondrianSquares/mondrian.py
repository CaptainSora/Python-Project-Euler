"""This module contains functions which produce theoretical arrangements of
rectangles.
"""
import numpy
import math
from itertools import combinations

# A Rect object is a numpy array [size, length, width]


def create_rect_list(size):
    """Returns an array of rect objects."""
    # The upper bound for rectangle objects.
    ceiling = math.ceil(size * size / 2)
    rect_list = numpy.array([], dtype=numpy.int32)
    for a in range(1, size + 1):
        for b in range(a, size + 1):
            if a * b > ceiling:
                break
            rect_list = numpy.append(rect_list, [a * b, a, b])
    rect_list = rect_list.reshape(-1, 3)
    numpy.sort(rect_list, axis=0)
    return rect_list


def find_permutation(size, numlist):
    """Returns all subsets of numlist which sum up to size^2"""
    valid = set()
    area = size * size
    for length in range(2, len(numlist)):
        comb_gen = combinations(numlist, length)
        for a in comb_gen:
            if sum(a) == area:
                valid.add(a)
    return valid


def search_sum(size, bound=0):
    """Returns all possible arrangements of rects with valid area"""
    if bound == 0:  # See oeis.org/A276523
        if size % 2 == 0:
            bound = math.ceil(size / math.log(size) + 3)
        else:
            bound = size
    rect_list = create_rect_list(size)
    size_list = rect_list[:, 0]  # View of rect_list
    # print(rect_list)
    valid = set()
    while True:
        # Search start index
        start = numpy.where(size_list >= size_list[-1] - bound)[0][0]
        valid |= find_permutation(size, size_list[start:])
        if start == 0:
            break
        size_list = [x for x in size_list if x < size_list[-1]]
    return valid


def defect(numset):
    return max(numset) - min(numset)


def min_theoretical_defect(size):
    all_sets = search_sum(size)
    tdefect = size
    while all_sets != set():
        subset = all_sets.pop()
        tdefect = min(tdefect, defect(subset))
    return tdefect

print([min_theoretical_defect(x) for x in range(3, 10)])
