def p1(data, stacks):
    for line in data:
        parts = line.split(" ")
        m, f, to = int(parts[1]), int(parts[3]), int(parts[5])
        for i in range(m):
            stacks[to] += stacks[f][-1]
            stacks[f] = stacks[f][:-1]
    s = ''
    for i in range(1, len(stacks) + 1):
        s += stacks[i][-1]
    return s


def p2(data, stacks):
    for line in data:
        parts = line.split(" ")
        m, f, to = int(parts[1]), int(parts[3]), int(parts[5])
        stacks[to] += stacks[f][-m:]
        stacks[f] = stacks[f][:-m]
    s = ''
    for i in range(1, len(stacks) + 1):
        s += stacks[i][-1]
    return s


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()][10:]
    stacks = {1: 'VCDRZGBW', 2: 'GWFCBSTV', 3: 'CBSNW', 4: 'QGMNJVCP', 5: 'TSLFDHB', 6: 'JVTWMN', 7: 'PFLCSTG',
              8: 'BDZ', 9: 'MNZW'}
    print(f'Part 1 : {p1(data, stacks)}')
    stacks = {1: 'VCDRZGBW', 2: 'GWFCBSTV', 3: 'CBSNW', 4: 'QGMNJVCP', 5: 'TSLFDHB', 6: 'JVTWMN', 7: 'PFLCSTG',
              8: 'BDZ', 9: 'MNZW'}  # Fuck you Python
    print(f'Part 2 : {p2(data, stacks)}')
