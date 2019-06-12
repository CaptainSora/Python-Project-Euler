"""This module attempts to solve the first half of the Mondrian Squares
Problem.
"""
import math
import time
import heapq
import json


def area(rect):
    """Calculates the area of a rectangle."""
    return rect[0] * rect[1]


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


# ============================================================================
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
            print(f"Searching tree {i + 1} of {len(rect_list)}, n = {size}")
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


def defect(rectlist):
    """Returns the defect of a rectlist."""
    arealist = [area(x) for x in rectlist]
    return max(arealist) - min(arealist)


def write_part_1(size, stop=0, improve=True, quiet=False):
    """Solves part 1 of the Mondrian Squares problem and saves the results to
    file.

    size: the side length of the square
    improve: whether to search only for current best or better solutions
    """
    if stop == 0:
        stop = size + 1
    for n in range(size, stop):
        bound = 0
        if improve:
            bound = optimal(n)
        else:
            resp = input("Are you sure you want suboptimal values?? [Y/N]")
            if resp != "Y" and resp != "y":
                print("Aborted.")
                return None
        solutionlist = search_sum(n, bound, quiet)
        solutiondict = {}
        for a in solutionlist:
            d = defect(a)
            if d < bound:
                # print(f"Found smaller defect in size {n}!")
                pass
            if str(d) not in solutiondict:
                solutiondict[str(d)] = []
            solutiondict[str(d)].append(a)
        f = open(f"MondrianSquares/Part1/length{n:03}.json", "w+")
        f.write(json.dumps(solutiondict))
        f.close()
        if not quiet:
            print("Saved to file.")


# ============ THE REAL PART 2 ===============================================
def find_tiling(rectlist):
    pass


def search_tiling(size):
    f = open(f"MondrianSquares/Part1/length{size:03}", 'r')
    solutiondict = json.load(f)
    f.close()
    keylist = [x for x in solutiondict]
    keylist.sort()

    for a in keylist:
        solutionlist = solutiondict[a]
        for b in solutionlist:
            if find_tiling(b):
                print("Eureka!")

