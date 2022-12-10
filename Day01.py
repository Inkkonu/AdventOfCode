def p1(data):
    return data[-1]


def p2(data):
    return sum(data[-3:])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [''] + [int(line.strip()) if line.strip() != '' else '' for line in f.readlines()]
        x = [i for i, s in enumerate(data) if s == '']
        y = x[1:] + [len(data)]
        data = sorted(list(map(sum, [data[i + 1:j] for i, j in zip(x, y)])))
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
