def p1(data):
    t = 0
    for line in data:
        parts = line.split(' ')
        mini, maxi = int(parts[0].split('-')[0]), int(parts[0].split('-')[1])
        c = parts[1][0]
        pwd = parts[2]
        if mini <= pwd.count(c) <= maxi:
            t += 1
    return t


def p2(data):
    t = 0
    for line in data:
        parts = line.split(' ')
        mini, maxi = int(parts[0].split('-')[0]) - 1, int(parts[0].split('-')[1]) - 1
        c = parts[1][0]
        pwd = parts[2]
        if (pwd[mini] == c) != (pwd[maxi] == c):
            t += 1
    return t


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
