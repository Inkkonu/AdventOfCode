def p1(data):
    xTail, yTail = 0, 0
    xHead, yHead = 0, 0
    seen = {(xTail, yTail)}
    for line in data:
        direction, length = line[0], int(line[2:])
        for i in range(length):
            if direction == 'R':
                xHead += 1
            elif direction == 'L':
                xHead -= 1
            elif direction == 'U':
                yHead += 1
            elif direction == 'D':
                yHead -= 1

            if xHead == xTail + 2 and yHead == yTail:
                xTail += 1
            elif xHead == xTail - 2 and yHead == yTail:
                xTail -= 1
            elif yHead == yTail + 2 and xHead == xTail:
                yTail += 1
            elif yHead == yTail - 2 and xHead == xTail:
                yTail -= 1
            elif xHead == xTail + 1 and yHead == yTail + 2:
                xTail += 1
                yTail += 1
            elif xHead == xTail + 1 and yHead == yTail - 2:
                xTail += 1
                yTail -= 1
            elif xHead == xTail - 1 and yHead == yTail + 2:
                xTail -= 1
                yTail += 1
            elif xHead == xTail - 1 and yHead == yTail - 2:
                xTail -= 1
                yTail -= 1
            elif xHead == xTail + 2 and yHead == yTail + 1:
                xTail += 1
                yTail += 1
            elif xHead == xTail + 2 and yHead == yTail - 1:
                xTail += 1
                yTail -= 1
            elif xHead == xTail - 2 and yHead == yTail - 1:
                xTail -= 1
                yTail -= 1
            elif xHead == xTail - 2 and yHead == yTail + 1:
                xTail -= 1
                yTail += 1
            seen.add((xTail, yTail))
    return len(seen)


def p2(data):
    tails = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    xTail, yTail = tails[0]
    xHead, yHead = 0, 0
    seen = {(xTail, yTail)}
    for line in data:
        direction, length = line[0], int(line[2:])
        for i in range(length):
            if direction == 'R':
                xHead += 1
            elif direction == 'L':
                xHead -= 1
            elif direction == 'U':
                yHead += 1
            elif direction == 'D':
                yHead -= 1

            if xHead == xTail + 2 and yHead == yTail:
                xTail += 1
            elif xHead == xTail - 2 and yHead == yTail:
                xTail -= 1
            elif yHead == yTail + 2 and xHead == xTail:
                yTail += 1
            elif yHead == yTail - 2 and xHead == xTail:
                yTail -= 1
            elif xHead == xTail + 1 and yHead == yTail + 2:
                xTail += 1
                yTail += 1
            elif xHead == xTail + 1 and yHead == yTail - 2:
                xTail += 1
                yTail -= 1
            elif xHead == xTail - 1 and yHead == yTail + 2:
                xTail -= 1
                yTail += 1
            elif xHead == xTail - 1 and yHead == yTail - 2:
                xTail -= 1
                yTail -= 1
            elif xHead == xTail + 2 and yHead == yTail + 1:
                xTail += 1
                yTail += 1
            elif xHead == xTail + 2 and yHead == yTail - 1:
                xTail += 1
                yTail -= 1
            elif xHead == xTail - 2 and yHead == yTail - 1:
                xTail -= 1
                yTail -= 1
            elif xHead == xTail - 2 and yHead == yTail + 1:
                xTail -= 1
                yTail += 1
            tails[0] = (xTail, yTail)

            for i in range(1, len(tails)):
                xHeadTemp, yHeadTemp, xTailTemp, yTailTemp = tails[i - 1][0], tails[i - 1][1], tails[i][0], tails[i][1]
                if xHeadTemp == xTailTemp + 2 and yHeadTemp == yTailTemp:
                    xTailTemp += 1
                elif xHeadTemp == xTailTemp - 2 and yHeadTemp == yTailTemp:
                    xTailTemp -= 1
                elif yHeadTemp == yTailTemp + 2 and xHeadTemp == xTailTemp:
                    yTailTemp += 1
                elif yHeadTemp == yTailTemp - 2 and xHeadTemp == xTailTemp:
                    yTailTemp -= 1
                elif xHeadTemp == xTailTemp + 1 and yHeadTemp == yTailTemp + 2:
                    xTailTemp += 1
                    yTailTemp += 1
                elif xHeadTemp == xTailTemp + 1 and yHeadTemp == yTailTemp - 2:
                    xTailTemp += 1
                    yTailTemp -= 1
                elif xHeadTemp == xTailTemp - 1 and yHeadTemp == yTailTemp + 2:
                    xTailTemp -= 1
                    yTailTemp += 1
                elif xHeadTemp == xTailTemp - 1 and yHeadTemp == yTailTemp - 2:
                    xTailTemp -= 1
                    yTailTemp -= 1
                elif xHeadTemp == xTailTemp + 2 and yHeadTemp == yTailTemp + 1:
                    xTailTemp += 1
                    yTailTemp += 1
                elif xHeadTemp == xTailTemp + 2 and yHeadTemp == yTailTemp - 1:
                    xTailTemp += 1
                    yTailTemp -= 1
                elif xHeadTemp == xTailTemp - 2 and yHeadTemp == yTailTemp - 1:
                    xTailTemp -= 1
                    yTailTemp -= 1
                elif xHeadTemp == xTailTemp - 2 and yHeadTemp == yTailTemp + 1:
                    xTailTemp -= 1
                    yTailTemp += 1
                elif xHeadTemp == xTailTemp + 2 and yHeadTemp == yTailTemp + 2:
                    xTailTemp += 1
                    yTailTemp += 1
                elif xHeadTemp == xTailTemp + 2 and yHeadTemp == yTailTemp - 2:
                    xTailTemp += 1
                    yTailTemp -= 1
                elif xHeadTemp == xTailTemp - 2 and yHeadTemp == yTailTemp + 2:
                    xTailTemp -= 1
                    yTailTemp += 1
                elif xHeadTemp == xTailTemp - 2 and yHeadTemp == yTailTemp - 2:
                    xTailTemp -= 1
                    yTailTemp -= 1
                tails[i] = (xTailTemp, yTailTemp)
                seen.add((tails[-1][0], tails[-1][1]))
    return len(seen)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
