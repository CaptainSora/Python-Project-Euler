import math

# diophantine(d) finds the smalles value of x such that x^2 - dy^2 = 1, for positive integers x and y.
def diophantine(d):
    x = 2
    while True:
        y = math.floor(math.sqrt((x**2 - 1)/d))
        while True:
            result = (x * x) - (d * y * y)
            if result > 1:
                y += 1
                continue
            elif result == 1:
                return x
            else:
                break
        x += 1

# minimal_x(ceiling) returns the value of d which requires the highest x in its diophantine equation.
def minimal_x(ceiling):
    # FAILS ON 61
    max_x = 0
    max_d = 0
    squares = set([x ** 2 for x in range(math.floor(math.sqrt(ceiling))+1)])
    for d in range(2, ceiling + 1):
        if d not in squares:
            print("testing d =", d)
            x = diophantine(d)
            if x > max_x:
                max_x = x
                max_d = d
    print(max_d)

#minimal_x(1000)