def p1(data, replace=True):
    i = 0
    if replace:
        data[1] = 12
        data[2] = 2
    while i < len(data):
        opcode = data[i]
        if opcode == 99:
            return data[0]
        a, b, c = data[data[i + 1]], data[data[i + 2]], data[i + 3]
        if opcode == 1:
            data[c] = a + b
        if opcode == 2:
            data[c] = a * b
        i += 4


def p2(data):
    for i in range(100):
        for j in range(100):
            data[1] = i
            data[2] = j
            if p1(data[:], False) == 19690720:
                return 100 * i + j


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [int(line.strip()) for line in f.readlines()[0].split(',')]
    print(f'Part 1 : {p1(data)}')
    with open('input.txt', 'r') as f:
        data = [int(line.strip()) for line in f.readlines()[0].split(',')]
    print(f'Part 2 : {p2(data)}')
