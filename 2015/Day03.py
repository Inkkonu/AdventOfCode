def p1(data):
    x = y = 0
    seen = {(x, y)}
    for d in data[0]:
        match d:
            case '<':
                x -= 1
            case '>':
                x += 1
            case '^':
                y += 1
            case 'v':
                y -= 1
        seen.add((x, y))
    return len(seen)


def p2(data):
    t = 0
    xSanta = ySanta = xRobot = yRobot = 0
    seen = {(0, 0)}
    for i, d in enumerate(data[0]):
        match d:
            case '<':
                if i%2==0:
                    xSanta -= 1
                else:
                    xRobot -= 1
            case '>':
                if i % 2 == 0:
                    xSanta += 1
                else:
                    xRobot += 1
            case '^':
                if i % 2 == 0:
                    ySanta += 1
                else:
                    yRobot += 1
            case 'v':
                if i % 2 == 0:
                    ySanta -= 1
                else:
                    yRobot -= 1
        seen.add((xSanta, ySanta))
        seen.add((xRobot, yRobot))
    return len(seen)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
