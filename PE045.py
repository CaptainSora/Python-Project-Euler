def in_all(min_val):
    """
    Finds the first number greater than min_val which is triangular,
    pentagonal, and hexagonal.
    """
    tri = [1, 3]
    pent = [1, 5]
    hexa = [1, 6]
    # Start after min_val
    while tri[-1] <= min_val:
        tri.append(int(len(tri) * (len(tri) + 1) / 2))
    # Loop to find num
    while True:
        while tri[-1] > pent[-1]:
            pent.append(int(len(pent) * (3 * len(pent) - 1) / 2))
        while tri[-1] > hexa[-1]:
            hexa.append(len(hexa) * (2 * len(hexa) - 1))
        if tri[-1] in pent and tri[-1] in hexa:
            if vol >= 1:
                print(tri[-1])
            if tri[-1] > min_val:
                if vol >= 1:
                    print(f"{tri[-1]} is tri/pent/hexagonal.")
                return tri[-1]
        tri.append(int(len(tri) * (len(tri) + 1) / 2))


def solve(vol=0):
    return in_all(40755)
