from collections import Counter


def isFive(hand):
    hand = sorted(hand)
    return hand[0] == hand[-1]


def canBeSomething(hand, valueOrder, func):
    for i in range(len(hand)):
        if hand[i] == "J":
            for v in valueOrder[:-1]:
                if canBeSomething(hand[0:i] + v + hand[i + 1:], valueOrder, func):
                    return True
    return func(hand)


def isFour(hand):
    c = Counter(hand)
    return 4 in c.values() and 1 in c.values()


def isHouse(hand):
    c = Counter(hand)
    return 3 in c.values() and 2 in c.values()


def isThree(hand):
    c = Counter(hand)
    return 3 in c.values() and list(c.values()).count(1) == 2


def isTwo(hand):
    c = Counter(hand)
    return 1 in c.values() and list(c.values()).count(2) == 2


def isOne(hand):
    c = Counter(hand)
    return 2 in c.values() and list(c.values()).count(1) == 3


def isHigh(hand):
    c = Counter(hand)
    return list(c.values()).count(1) == 5


def p1(data):
    def valueIsStronger(v1, v2):
        valueOrder = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        return -(valueOrder.index(v1) - valueOrder.index(v2))

    def handIsStronger(h1, h2):
        for v1, v2 in zip(h1, h2):
            c = valueIsStronger(v1, v2)
            if c != 0:
                return c
        return 0

    def bubbleSort(array):
        n = len(array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if handIsStronger(array[j][0], array[j + 1][0]) < 0:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    fives, fours, houses, threes, twos, ones, highs = [], [], [], [], [], [], []
    for line in data:
        line = line.split()
        hand = line[0]
        bid = int(line[1])
        if isFive(hand):
            fives.append((hand, bid))
        if isFour(hand):
            fours.append((hand, bid))
        if isHouse(hand):
            houses.append((hand, bid))
        if isThree(hand):
            threes.append((hand, bid))
        if isTwo(hand):
            twos.append((hand, bid))
        if isOne(hand):
            ones.append((hand, bid))
        if isHigh(hand):
            highs.append((hand, bid))

    fives = bubbleSort(fives)
    fours = bubbleSort(fours)
    houses = bubbleSort(houses)
    threes = bubbleSort(threes)
    twos = bubbleSort(twos)
    ones = bubbleSort(ones)
    highs = bubbleSort(highs)

    allHands = fives + fours + houses + threes + twos + ones + highs
    allHands = allHands[::-1]

    return sum([(i + 1) * allHands[i][1] for i in range(len(allHands))])


def p2(data):
    valueOrder = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    def valueIsStronger(v1, v2):
        return -(valueOrder.index(v1) - valueOrder.index(v2))

    def handIsStronger(h1, h2):
        for v1, v2 in zip(h1, h2):
            c = valueIsStronger(v1, v2)
            if c != 0:
                return c
        return 0

    def bubbleSort(array):
        n = len(array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if handIsStronger(array[j][0], array[j + 1][0]) < 0:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    fives, fours, houses, threes, twos, ones, highs = [], [], [], [], [], [], []
    for line in data:
        line = line.split()
        hand = line[0]
        bid = int(line[1])
        if isFive(hand) or canBeSomething(hand, valueOrder, isFive):
            fives.append((hand, bid))
        elif isFour(hand) or canBeSomething(hand, valueOrder, isFour):
            fours.append((hand, bid))
        elif isHouse(hand) or canBeSomething(hand, valueOrder, isHouse):
            houses.append((hand, bid))
        elif isThree(hand) or canBeSomething(hand, valueOrder, isThree):
            threes.append((hand, bid))
        elif isTwo(hand) or canBeSomething(hand, valueOrder, isTwo):
            twos.append((hand, bid))
        elif isOne(hand) or canBeSomething(hand, valueOrder, isOne):
            ones.append((hand, bid))
        elif isHigh(hand):
            highs.append((hand, bid))

    fives = bubbleSort(fives)
    fours = bubbleSort(fours)
    houses = bubbleSort(houses)
    threes = bubbleSort(threes)
    twos = bubbleSort(twos)
    ones = bubbleSort(ones)
    highs = bubbleSort(highs)

    allHands = fives + fours + houses + threes + twos + ones + highs
    allHands = allHands[::-1]

    return sum([(i + 1) * allHands[i][1] for i in range(len(allHands))])


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
