import itertools
from int_tools import int_to_str_array

### WARNING LONG PROGRAM

searchlen = 8

# count(numlist) produces an array of size (10 - searchlen + 1) which returns indices of the
#   digits 0, 1, ... (10 - searchlen) within the digit array.
# usage: the smallest member of the prime family must include one of these digits.
def count(numlist):
    indexarray = []
    for a in range(10 - searchlen + 1):
        indexes = []
        for b in range(len(numlist)):
            if int(numlist[b]) == a:
                indexes.append(b)
        indexarray.append(indexes)
    return indexarray


# families(num) produces an array where each element is a possible family of num.
#   Each family is stored as an array.
def families(num):
    indexarray = count(int_to_str_array(num))
    familiesarray = []
    for digit_indices in indexarray:
        for b in range(1, len(digit_indices) + 1):
            # permutation of length b
            replacements = itertools.combinations(digit_indices, b)
            for c in replacements:
                numarray = int_to_str_array(num)
                for d in c:
                    numarray[d] = '*'
                familiesarray.append(numarray)
    return familiesarray


# familysize(num) produces True if num is part of a family which meets the minimum size searchlen.
def familysize(num):
    numsize = len(str(num))
    familyarray = families(num)
    for family in familyarray:
        counter = 0
        minprime = 0
        for digit in range(10):
            # Python requires the list call otherwise it will just point to the same object
            newnum = list(family)
            for a in range(len(newnum)):
                if newnum[a] == '*':
                    newnum[a] = str(digit)
            newnum = int(''.join(newnum))
            if len(str(newnum)) == numsize and newnum in primes:
                counter += 1
                if minprime == 0:
                    minprime = newnum
        if counter == searchlen:
            print("Found family of length %d starting with %d" % (counter, minprime))
            return True

'''
for a in primes:
    print(a)
    if familysize(a):
        break
'''

familysize(121313)