def p1(data, d):
    return sum([d[c.pop()] for c in [set(line[:len(line)//2]).intersection(set(line[len(line)//2:])) for line in data]])


def p2(data, d):
    return sum([d[c.pop()] for c in [set(data[i]).intersection(set(data[i+1]), set(data[i+2])) for i in range(0, len(data), 3)]])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    d = dict()
    for i in range(1, 27):
        d[chr(ord('a') - 1 + i)] = i
        d[chr(ord('A') - 1 + i)] = i + 26
    print(f'Part 1 : {p1(data, d)}')
    print(f'Part 2 : {p2(data, d)}')