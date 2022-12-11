def p1(data):
    t = 0
    for line in data:
        l, w, h = int(line.split('x')[0]), int(line.split('x')[1]), int(line.split('x')[2])
        t += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
    return t


def p2(data):
    t = 0
    for line in data:
        l, w, h = int(line.split('x')[0]), int(line.split('x')[1]), int(line.split('x')[2])
        t += 2 * sorted([l, w, h])[0] + 2 * sorted([l, w, h])[1] + l * w * h
    return t


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
