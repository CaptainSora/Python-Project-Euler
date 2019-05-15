import collections

f = open('p054_poker.txt', 'r')

rawcards = f.read().split()

cardorder = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
handorder = ['SF', '4K', 'FH', 'FL', 'ST', '3K', '2P', '1P', 'HC']

p1 = []
p2 = []

for a in range(int(len(rawcards)/10)):
    p1.append(rawcards[10*a:10*a+5])
    p2.append(rawcards[10*a+5:10*a+10])

# replace me
def tiebreak(hand1, hand2):
    values1 = [x[0] for x in hand1]
    values2 = [x[0] for x in hand2]
    diff = list(set(values1) ^ set(values2))
    diff.sort(key=cardorder.index)
    if diff[0] in values1:
        return 1
    elif diff[0] in values2:
        return 0


def high_card(hand):
    for a in cardorder:
        if a in [x[0] for x in hand]:
            return a


def valuesearch(hand):
    values = [x[0] for x in hand]
    valcopy = list(dict.fromkeys(values))
    diff = list(values)
    for a in valcopy:
        diff.remove(a)
    # sorted in descending order
    diff.sort(key=cardorder.index)
    if len(diff) == 0:
        return "HC" + high_card(hand)
    elif len(diff) == 1:
        return "1P" + diff[0]
    elif len(diff) == 2:
        # Two pair or Three of a kind
        if diff[0] == diff[1]:
            return "3K" + diff[0]
        else:
            return "2P" + diff[0] + diff[1]
    elif len(diff) == 3:
        # Full House or Four of a Kind
        if diff[0] == diff[1] == diff[2]:
            return "4K" + diff[0]
        else:
            return "FH" + collections.Counter(diff).most_common(1)[0][0]


def flushsearch(hand):
    suits = [x[1] for x in hand]
    suitcopy = list(dict.fromkeys(suits))
    if len(suitcopy) == 1:
        return True
    return False


def straightsearch(hand):
    values = [x[0] for x in hand]
    values.sort(key=cardorder.index)
    startindex = cardorder.index(values[0])
    if startindex > 8: # highest card < 6
        return ""
    for a in range(1, 5):
        if values[a] != cardorder[startindex + a]:
            return ""
    return "ST" + values[0]


def besthand(hand):
    flush = flushsearch(hand)
    straight = straightsearch(hand)
    value = valuesearch(hand)
    if flush and straight != "":
        return "SF" + straight[2]
    elif value[:2] == "4K" or value[:2] == "FH":
        return value
    elif flush:
        return "FL2"
    elif straight != "":
        return straight
    else:
        return value


def winner(hand1, hand2):
    best = [besthand(hand1), besthand(hand2)]
    type = [handorder.index(x[:2]) for x in best]
    value = [cardorder.index(x[2]) for x in best]
    if type[0] < type[1]:
        return 1
    elif type[0] > type[1]:
        return 0
    elif value[0] < value[1]:
        return 1
    elif value[0] > value[1]:
        return 0
    else:
        diff = list(set(x[0] for x in hand1) ^ set(x[0] for x in hand2))
        diff.sort()
        if diff[0] in [x[0] for x in hand1]:
            return 1
        else:
            return 0


wincounter = 0
for a in range(len(p1)):
    wincounter += winner(p1[a], p2[a])

print(wincounter)
