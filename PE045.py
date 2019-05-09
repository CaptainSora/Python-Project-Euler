tri = [1]
tri_len = 1
pent = [1]
pent_len = 1
hexa = [1]
hexa_len = 1

def next(val):
    global tri, tri_len, pent, pent_len, hexa, hexa_len
    if val == 3:
        tri_len += 1
        tri.append(tri_len * (tri_len + 1) / 2)
    elif val == 5:
        pent_len += 1
        pent.append(pent_len * (3 * pent_len - 1) / 2)
    elif val == 6:
        hexa_len += 1
        hexa.append(hexa_len * (2 * hexa_len - 1))

def in_all(min_val):
    next(3)
    while True:
        while tri[-1] > pent[-1]:
            next(5)
        while tri[-1] > hexa[-1]:
            next(6)
        if tri[-1] in pent and tri[-1] in hexa:
            print(tri[-1])
            if tri[-1] > min_val:
                print("Done!")
                break
        next(3)

in_all(40755)
