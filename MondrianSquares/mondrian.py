"""This module contains functions which produce theoretical arrangements of
rectangles.
"""
import numpy
import math
from itertools import combinations
import time

# Notes
# Time it with and without sorting
# in search_sum while loop, should be able to continue if this loop is a
#   strict subset of the previous loop


# A Rect object is a numpy array [size, length, width]


def defect(numset):
    """Returns the defect of a set."""
    return max(numset) - min(numset)


def optimal(size):
    """Returns a(n) for 3 <= n <= 57 where a(n) is the optimal tiling of the
    Mondrian Art Puzzle.
    """
    OEIS = [
        0, 0, 0, 2, 4, 4, 5, 5, 6, 6, 8, 6, 7, 8, 6, 8, 8, 8, 8, 8, 9, 9, 9,
        8, 9, 10, 9, 10, 9, 9, 11, 11, 10, 12, 12, 11, 12, 11, 10, 11, 12, 13,
        12, 12, 12, 13, 13, 12, 14, 12, 13, 14, 13, 14, 15, 14, 14, 15
    ]
    return OEIS[size]


def create_rect_list(size):
    """Returns an array of rect objects for the size x size square."""
    # The upper bound for rectangle objects.
    ceiling = math.ceil(size * size / 2)
    rect_list = numpy.array([], dtype=numpy.uint8)
    for a in range(1, size + 1):
        for b in range(a, size + 1):
            if a * b > ceiling:
                break
            rect_list = numpy.append(rect_list, [a * b, a, b])
    rect_list = rect_list.reshape(-1, 3)
    """
    print("Rectangle list generation complete")
    """
    return rect_list


def find_subset(size, numlist):
    """Returns all subsets of numlist which sum up to size^2"""
    valid = set()
    area = size * size
    for length in range(2, len(numlist)):
        comb_gen = combinations(numlist, length)
        for a in comb_gen:
            if sum(a) == area:
                # print("Found a subset", a)
                valid.add(a)
    return valid


# Uses create_rect_list, find_subset
def search_sum(size, bound=0):
    """Returns all possible arrangements of rects with valid area"""
    if bound == 0:  # See oeis.org/A276523
        if size % 2 == 0:
            bound = math.ceil(size / math.log(size) + 3)
        else:
            bound = size
    rect_list = create_rect_list(size)
    size_list = rect_list[:, 0]  # View of rect_list
    valid = set()
    lower = 0
    while True:
        searchlist = [x for x in size_list if x >= size_list[-1] - bound]
        # Check if range overlaps
        if searchlist[0] != lower:
            # Search start index
            """
            print(f"Searching range {searchlist[0]} to {searchlist[-1]}")
            """
            valid |= find_subset(size, searchlist)
            if size_list[-1] <= bound + 1:
                break
        lower = searchlist[0]
        size_list = [x for x in size_list if x < size_list[-1]]
    # print(rect_list)
    return [rect_list, valid]


# Uses: search_sum
def min_theoretical_defect(size):
    all_sets = search_sum(size)
    tdefect = size
    while all_sets != set():
        subset = all_sets.pop()
        tdefect = min(tdefect, defect(subset))
    return tdefect


# Deprecated
def subsetsum(sum, rectlist):
    nlist = []
    rectsize = len(rectlist)
    for i in range(rectsize):
        area = rectlist[i][0] * rectlist[i][1]
        if area < sum:
            rlist = subsetsum(sum - area, rectlist[i + 1:])
            for a in rlist:
                a.append([rectlist[i]])
                nlist.append(a)
        elif area == sum:
            nlist.append([rectlist[i]])
    return nlist
