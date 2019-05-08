
# n_digit_power() returns the number of n-digit positive integers which are also nth powers.
def n_digit_power():
    counter = 0
    powlen = 1
    while True:
        base = 1
        while True:
            if len(str(base ** powlen)) == powlen:
                counter += 1
            elif len(str(base ** powlen)) > powlen:
                break
            base += 1
        powlen += 1
        if len(str(9 ** powlen)) < powlen:
            break
    print(counter)

n_digit_power()