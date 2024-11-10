def p1(data):
    return sum([int(data[i]) for i in range(len(data)) if data[i] == data[(i + 1) % len(data)]])


def p2(data):
    return sum([int(data[i]) for i in range(len(data)) if data[i] == data[(i + len(data) // 2) % len(data)]])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()][0]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
