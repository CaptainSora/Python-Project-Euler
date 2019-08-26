ENGDICT = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


def letter_count():
    """
    Returns the number of letters used in all the numbers between 1 and 1000
    inclusive, not counting spaces or hyphens, following British standard.
    """
    count = 0
    for i in range(1, 1001):
        if i % 100 < 20:
            count += len(ENGDICT[i % 100])
        else:
            count += len(ENGDICT[i % 10])
            count += len(ENGDICT[i % 100 - i % 10])
        if 100 <= i < 1000:
            if i % 100 > 0:
                count += len('and')
            count += len(ENGDICT[100])
            count += len(ENGDICT[i // 100])
        elif i == 1000:
            count += len(ENGDICT[1] + ENGDICT[1000])
    return count


def solve(vol=0):
    return letter_count()
