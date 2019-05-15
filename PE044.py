
pentagonal = [1]
pent_len = 1

def next():
    global pentagonal, pent_len
    pent_len += 1
    pentagonal.append(pent_len * (3 * pent_len - 1) / 2)

def min_diff():
    global pentagonal
    next()
    index = 1
    min_diff = 0
    while True:
        for a in range(index):
            summ = pentagonal[index] + pentagonal[a]
            diff = pentagonal[index] - pentagonal[a]
            while (summ > pentagonal[-1]) :
                next()
            if summ in pentagonal and diff in pentagonal:
                if diff < min_diff or min_diff == 0:
                    min_diff = diff
        req_diff = pentagonal[index + 1] - pentagonal[index]
        if 0 < min_diff: # technically should also brute force verify that min_diff < req_diff
            break
        else:
            print("Tested %d min_diff %d required %d" % (pentagonal[index], min_diff, req_diff))
            index += 1
    print("D is %d" % min_diff)

min_diff()