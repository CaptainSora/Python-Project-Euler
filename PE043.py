from _pandigital_tools import generate


def substring_div(vol=0):
    primes = [2, 3, 5, 7, 11, 13, 17]
    sum = 0
    pandigital = generate(0, 9)
    for a in pandigital:
        property = True
        for b in range(7):
            if int(str(a)[b+1:b+4]) % primes[b] != 0:
                property = False
                break
        if property:
            sum += a
            if vol >= 2:
                print(a)
    if vol >= 1:
        print("sum is %d" % sum)
    return sum


def solve(vol=0):
    return substring_div(vol=vol)
