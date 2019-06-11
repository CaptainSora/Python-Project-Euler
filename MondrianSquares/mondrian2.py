"""This module attempts to solve the first half of the Mondrian Squares
Problem.
"""
import math
import time
import heapq


def area(rect):
    """Calculates the area of a rectangle."""
    return rect[0] * rect[1]


def create_rect_list(size, quiet=False, generator=True):
    """Returns a generator or an array of rect objects for the size x size 
    square. Faster than sorting.
    """
    # The upper bound for rectangle objects.
    ceiling = math.ceil(size * size / 2)
    rect_list = []
    for a in range(1, size + 1):
        temp_list = []
        for b in range(a, size + 1):
            if a * b > ceiling:
                break
            temp_list.append((a, b))
        rect_list = heapq.merge(rect_list, temp_list, key=area)
    if not quiet:
        print("Rectangle list generation complete")
    if generator:
        return rect_list
    else:
        return [x for x in rect_list]


def search_sum(size, bound=0, quiet=False, index=False):
    """Returns all possible arrangements of rects with valid area"""
    if bound == 0:  # See oeis.org/A276523
        if size % 2 == 0:
            bound = math.ceil(size / math.log(size) + 3)
        else:
            bound = size
    rect_list = create_rect_list(size, quiet, generator=False)

    def subsetsum(sum, start, lower):
        """Recursive tree search for total subset size"""
        subset = []
        for i in range(len(rect_list) - start):
            a = area(rect_list[i + start])
            if a - lower > bound or a > sum:
                # Depth exceeded or value too large
                break
            elif a < sum:
                # Recursion
                rlist = subsetsum(sum - a, i + start + 1, lower)
                for r in rlist:
                    if index:
                        r.append(i + start)
                    else:
                        r.append(rect_list[i + start])
                    subset.append(r)
            elif a == sum:
                # Base case
                if index:
                    subset.append([i + start])
                else:
                    subset.append([rect_list[i + start]])
        return subset

    solutionlist = []
    for i in range(len(rect_list)):
        if not quiet:
            print(f"Searching tree {i + 1} of {len(rect_list)}")
        a = area(rect_list[i])
        rlist = subsetsum(size * size - a, i + 1, a)
        for r in rlist:
            if index:
                r.append(i)
            else:
                r.append(rect_list[i])
        solutionlist.extend(rlist)

    if not quiet:
        print(f"Found {len(solutionlist)} possible solutions")
    return solutionlist


def count_time(value, quiet=False):
    """Returns the running times of start through stop inclusive."""
    if not quiet:
        print("Searching size", value)
    timestart = time.perf_counter()
    search_sum(value, quiet)
    duration = round(time.perf_counter() - timestart, 3)
    if not quiet:
        print(f"Size {value} takes {duration} s.")
    return duration


def find_duplicates(size):
    """Temporary function"""
    rect_list = create_rect_list(size, quiet=True, generator=False)
    solutionlist = search_sum(size)
    indexlist = []
    for a in solutionlist:
        templist = []
        for b in a:
            templist.append(rect_list.index(b))
        templist.sort()
        indexlist.append(templist)
    print(indexlist)

count_time(15)
