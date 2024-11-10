def p1(data):
    return sum([1 if c == '(' else -1 for c in data[0]])


def p2(data):
    f = 0
    for i, c in enumerate(data[0]):
        f += 1 if c == '(' else -1
        if f == -1:
            return i+1


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
