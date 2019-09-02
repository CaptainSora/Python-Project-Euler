COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def coin_sums(target):
    """
    Returns the number of ways that target can be made using only the
    denominations found in COINS.
    """
    # csums[n][m] holds the number of ways that n can be made with highest
    #   denomination m.
    csums = [[0] * len(COINS)]
    while len(csums) <= target:
        tempsum = [0] * len(COINS)
        for a in range(len(COINS)):
            if COINS[a] > len(csums):
                break
            elif COINS[a] == len(csums):
                tempsum[a] = 1
            else:
                tempsum[a] += sum(csums[len(csums) - COINS[a]][:a+1])
        csums.append(tempsum)
    return sum(csums[target])


def solve(vol=0):
    return coin_sums(200)
