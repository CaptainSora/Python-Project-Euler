sum = 0

for a in range(1, 1001):
    sum += a**a
    sum %= 10**10

print(sum)