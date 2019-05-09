from primalitytest import factor

# WARNING LONG PROGRAM: VALUES CHANGED TO RESULT

def count_factors(num):
    factors = factor(num)
    # dictionaries cannot have duplicate values
    factors = list(dict.fromkeys(factors))
    return len(factors)


def consecutive(length):
    start = 134043
    while True:
        if count_factors(start) == length:
            print("Testing %d" % start)
            rest = True
            for a in range(1, length):
                if count_factors(start + a) != length:
                    rest = False
                    break
            if rest:
                print(start)
                break
        start += 1

consecutive(4)