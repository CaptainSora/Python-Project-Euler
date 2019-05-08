import math

# sqrt_period(n) returns the period of sqrt(n).
# requires n >= 0
def sqrt_period(n):
    x = math.floor(math.sqrt(n))
    f = [[x, 1, x]]
    if x == math.sqrt(n):
        return 0
    while True:
        next = [0, 0, 0]
        # MATH145 flashbacks
        next[1] = int((n - pow(f[-1][2], 2)) / f[-1][1])
        next[0] = math.floor((f[0][0] + f[-1][2]) / next[1])
        next[2] = next[0] * next[1] - f[-1][2]
        f.append(next)
        if len(f) > 2 and f[-1] == f[1]:
            return len(f)-2


# find_odd_period(ceiling) returns the number of continued fractions of sqrt(n) 
#   for n <= ceiling which have odd period.
def find_odd_period(ceiling):
    counter = 0
    for a in range(2, ceiling + 1):
        if sqrt_period(a) % 2 == 1:
            counter += 1
    print(counter)

find_odd_period(10000)