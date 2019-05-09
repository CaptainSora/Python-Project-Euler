import itertools

# generates a set of all pandigital numbers between start and stop inclusive
# requires: 0 <= start <= stop <= 9
def generate(start, stop):
    x = set(itertools.permutations(range(start, stop + 1), stop-start+1))
    newx = []
    for a in x:
        new = 0
        for b in a:
            new = 10 * new + b
        newx.append(new)
    return newx