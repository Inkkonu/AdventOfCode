from collections import defaultdict
import re
import time
from itertools import count


def p1(data):
    positions = defaultdict(int)
    width, height = 101, 103
    for line in data:
        if match := re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line):
            pX, pY, vX, vY = map(int, match.groups())
            pX = (pX + vX * 100) % width
            pY = (pY + vY * 100) % height
            positions[(pX, pY)] += 1
    first = second = third = fourth = 0
    for (x, y), count in positions.items():
        if 0 <= x < width // 2:
            if 0 <= y < height//2:
                first += count
            elif y > height // 2:
                third += count
        elif x > width//2:
            if 0 <= y < height//2:
                second += count
            elif y > height // 2:
                fourth += count
    return first*second*third*fourth


def p2(data):
    """
    WTF is this part 2
    The approach is : Move all robots. If there's a line of at least 21 robots in a row, display the grid and check whether this is the Christmas tree or not.
    The number is chosen because what we are looking for looks like this :

    *******************************
    *                             *
    *                             *
    *                             *
    *                             *
    *              *              *
    *             ***             *
    *            *****            *
    *           *******           *
    *          *********          *
    *            *****            *
    *           *******           *
    *          *********          *
    *         ***********         *
    *        *************        *
    *          *********          *
    *         ***********         *
    *        *************        *
    *       ***************       *
    *      *****************      *
    *        *************        *        
    *       ***************       *
    *      *****************      *
    *     *******************     *
    *    *********************    *
    *             ***             *
    *             ***             *
    *             ***             *
    *                             *
    *                             *
    *                             *
    *                             *
    *******************************
    """

    robots = []
    width, height = 101, 103
    for line in data:
        if match := re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line):
            pX, pY, vX, vY = map(int, match.groups())
            robots.append([pX, pY, vX, vY])
    for i in count(start=1):
        for robot in robots:
            robot[0] = (robot[0] + robot[2]) % width
            robot[1] = (robot[1] + robot[3]) % height
        isTree({(r[0], r[1]) for r in robots}, width, height)
    return 0


def isTree(positions, width, height):
    for (x, y) in positions:
        lineLength = 1
        i = 0
        while (x-i, y) in positions:
            lineLength += 1
            i += 1
        i = 0
        while (x+i, y) in positions:
            lineLength += 1
            i += 1

        if lineLength > 20:
            for y in range(height):
                for x in range(width):
                    if (x, y) in positions:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()
            time.sleep(3)  # To make sure I can see it


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
