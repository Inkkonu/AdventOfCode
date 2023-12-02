import re


def p1(data):
    d = {'red': 12, 'green': 13, 'blue': 14}
    totalIDs = 0
    for line in data:
        allSetsValid = True
        line = re.split(':|;', line)
        id = int(line[0].split(' ')[-1])
        for s in line[1:]:
            elems = s.split(',')
            for elem in elems:
                elem = elem.split(' ')
                color = elem[-1]
                allSetsValid &= (int(elem[1]) <= d[color])
        if allSetsValid:
            totalIDs += id
    return totalIDs


def p2(data):
    total = 0
    for line in data:
        d = {'red': 0, 'green': 0, 'blue': 0}
        line = re.split(':|;', line)
        id = int(line[0].split(' ')[-1])
        for s in line[1:]:
            elems = s.split(',')
            for elem in elems:
                elem = elem.split(' ')
                color = elem[-1]
                d[color] = max(d[color], int(elem[1]))
        total += d['red'] * d['green'] * d['blue']
    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
