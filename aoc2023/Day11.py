def p1(data):
    def double():
        i = 0
        l = len(data)
        while i < l:
            if all([x == '.' for x in data[i]]):
                data.insert(i, '.' * len(data[i]))
                i += 1
            i += 1
            l = len(data)
        return data

    double()
    data = list(zip(*data))[::]
    double()
    data = list(zip(*data))[::]

    galaxies = []
    for x, line in enumerate(data):
        for y, row in enumerate(line):
            if row == '#':
                galaxies.append((x, y))

    total = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            g1, g2 = galaxies[i], galaxies[j]
            total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    return total


def p2(data):
    def getEmpty():
        s = set()
        for i in range(len(data)):
            if all([x == '.' for x in data[i]]):
                s.add(i)
        return s

    emptyLines = getEmpty()
    data = list(zip(*data))[::]
    emptyColumns = getEmpty()
    data = list(zip(*data))[::]

    galaxies = []
    for x, line in enumerate(data):
        for y, row in enumerate(line):
            if row == '#':
                galaxies.append((x, y))

    total = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            g1, g2 = galaxies[i], galaxies[j]
            distance = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            miniX, maxiX = min(g1[0], g2[0]), max(g1[0], g2[0])
            miniY, maxiY = min(g1[1], g2[1]), max(g1[1], g2[1])
            distance += 999_999 * len([0 for x in emptyLines if miniX <= x <= maxiX])
            distance += 999_999 * len([0 for y in emptyColumns if miniY <= y <= maxiY])
            total += distance
    return total


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 2 : {p2(data)}')
