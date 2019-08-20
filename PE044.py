def min_diff(vol=0):
    """
    Calculates the minimum difference of any pair of pentagonal numbers whose
    sum and differences are also pentagonal.
    """
    # Equivalent to finding the smallest a such that:
    #   a, b, c, d are all pentagonal
    #   a + b = c
    #   b + c = d
    pent = [1, 5]
    index = 1
    min_diff = 0
    while True:
        for a in range(index):
            summ = pent[index] + pent[a]
            diff = pent[index] - pent[a]
            while (summ > pent[-1]):
                pent.append(int(len(pent) * (3 * len(pent) - 1) / 2))
            if summ in pent and diff in pent:
                if diff < min_diff or min_diff == 0:
                    min_diff = diff
        if 0 < min_diff:
            if vol >= 1:
                print("D is %d" % min_diff)
            return min_diff
        index += 1


def solve(vol=0):
    return min_diff(vol=vol)
