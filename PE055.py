def add_reverse(num):
    return num + int(''.join(list(str(num))[::-1]))

def is_palindrome(num):
    return (num == int(''.join(list(str(num))[::-1])))

def count_Lychrel(ceiling):
    count = 0
    for a in range(1, ceiling):
        testnum = a
        for b in range(50):
            if b == 49:
                count += 1
                break
            testnum = add_reverse(testnum)
            if is_palindrome(testnum):
                break
    return count

print(count_Lychrel(10000))