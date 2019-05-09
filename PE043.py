from pandigital import generate

def substring_div():
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
            print(a)
    print("sum is %d" % sum)

substring_div()

