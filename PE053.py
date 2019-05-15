import math

floor = 1000000

# requires n >= r
def nCr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

counter = 0
for n in range(1, 101):
    for r in range(n+1):
        if nCr(n, r) > floor:
            counter += 1

print(counter)