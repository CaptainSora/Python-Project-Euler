def sqrt_expansion(iter):
    counter = 0
    frac = [1, 1]
    for a in range(iter):
        frac = [frac[0] + 2 * frac[1], frac[0] + frac[1]]
        if len(str(frac[0])) > len(str(frac[1])):
            counter += 1
    print(counter)

sqrt_expansion(1000)