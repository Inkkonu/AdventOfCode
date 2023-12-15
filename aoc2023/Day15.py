def p1(data):
    total = 0
    for elem in data:
        current = 0
        for c in elem:
            current += ord(c)
            current *= 17
            current %= 256
        total += current
    return total


def hash(s):
    t = 0
    for c in s:
        t += ord(c)
        t *= 17
        t %= 256
    return t


def p2(data): # I learned after submitting that dictionaries are ordered since Python 3.7
    l = [[] for _ in range(256)]
    for elem in data:
        if elem[-1] == '-':
            label = elem[:-1]
            h = hash(label)
            for i in range(len(l[h])):
                if l[h][i].startswith(label):
                    del l[h][i]
                    break
        else:
            v = elem[-1]
            label = elem[:-2]
            h = hash(label)
            hasRemplaced = False
            for i in range(len(l[h])):
                if l[h][i].startswith(label):
                    l[h][i] = label + v
                    hasRemplaced = True
                    break
            if not hasRemplaced:
                l[h].append(label + v)

    total = 0
    for j in range(len(l)):
        for k in range(len(l[j])):
            total += (j + 1) * (k + 1) * int(l[j][k][-1])
    return total


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = [line.strip().split(',') for line in f.readlines()][0]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
