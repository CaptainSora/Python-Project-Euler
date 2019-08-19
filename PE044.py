def min_diff(vol=0):
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
        # req_diff = pent[index + 1] - pent[index]
        if 0 < min_diff:
            if vol >= 1:
                print("D is %d" % min_diff)
            return min_diff
        index += 1


def solve(vol=0):
    return min_diff(vol=vol)
