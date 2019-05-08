import math

# sum_digits(num) calculates the sum of the digits of num.
def sum_digits(num):
    total = 0
    for a in str(num)[:]:
        total += int(a)
    return total

# convergent_digits(cont_frac) produces the sum of the digits in the numerator of the partial continued fraction.
def convergent_digits(cont_frac):
    frac = [cont_frac[-1], 1]
    for x in cont_frac[-2::-1]:
        frac = frac[::-1]
        frac[0] += x * frac[1]
    print(sum_digits(frac[0]))

# e_frac(i) produces an array of the partial continued fraction representation of e up to i terms.
# requires: i > 0
def e_frac(i):
    frac = [2]
    for a in range(1, i):
        if a % 3 == 2:
            frac.append(int((a + 1) / 3 * 2))
        else:
            frac.append(1)
    return frac

convergent_digits(e_frac(100))