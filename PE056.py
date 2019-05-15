max_sum = 0

def sum_digits(num):
    numlist = list(str(num))
    return sum([int(x) for x in numlist])


for a in range(1, 100):
    for b in range(1, 100):
        cur_sum = sum_digits(a**b)
        max_sum = max(cur_sum, max_sum)

print(max_sum)