def p1(data):
    return sum([len(recurp1(data, start[0], start[1])) for start in findStarts(data)])


def recurp1(data, x, y):
    reachable = set()
    if data[x][y] == 9:
        reachable.add((x, y))
    else:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            newx, newy = x + dx, y+dy
            if 0 <= newx < len(data) and 0 <= newy < len(data[0]) and data[newx][newy] == data[x][y]+1:
                reachable.update(recurp1(data, newx, newy))
    return reachable


def findStarts(data):
    return set([(x, y) for x, line in enumerate(data) for y, v in enumerate(line) if v == 0])


def p2(data):
    return sum([len(recurp2(data, start[0], start[1])) for start in findStarts(data)])


def recurp2(data, x, y, path=set()):
    paths = list()
    if data[x][y] == 9:
        path.add((x, y))
        if path not in paths:
            paths.append(path)
    else:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            newx, newy = x + dx, y+dy
            if 0 <= newx < len(data) and 0 <= newy < len(data[0]) and data[newx][newy] == data[x][y]+1:
                path.add((x, y))
                paths += recurp2(data, newx, newy, path)
    return paths


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [list(map(int, line.strip())) for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
