def p1(data):
    return sum([max(line) - min(line) for line in data])


def p2(data):
    t = 0
    for line in data:
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                a, b = max(line[i], line[j]), min(line[i], line[j])
                if a % b == 0:
                    t += a // b
    return t


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [[int(n) for n in line.split("\t")] for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
