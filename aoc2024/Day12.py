import time


def p1(data):
    total = 0
    visited = set()
    for x, line in enumerate(data):
        for y, crop in enumerate(line):
            if (x, y) not in visited:
                region = getRegion(data, x, y, set())
                area = len(region)
                perimeter = getPerimeter(region)
                total += area * perimeter
                visited.update(region)
    return total


def getRegion(data, x, y, region):
    region.add((x, y))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        newX, newY = x + dx, y + dy
        if (
            0 <= newX < len(data)
            and 0 <= newY < len(data[0])
            and data[newX][newY] == data[x][y]
            and (newX, newY) not in region
        ):
            region.add((newX, newY))
            region.update(getRegion(data, newX, newY, region))
    return region


def getPerimeter(region):
    total = 0
    for x, y in region:
        perimeter = 4
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if (newX, newY) in region:
                perimeter -= 1
        total += perimeter
    return total


def p2(data):
    total = 0
    visited = set()
    for x, line in enumerate(data):
        for y, crop in enumerate(line):
            if (x, y) not in visited:
                region = getRegion(data, x, y, set())
                area = len(region)
                sides = getSides(region)
                total += area * sides
                visited.update(region)
    return total


def getSides(region):
    # Credits to encse's solution (https://aoc.csokavar.hu/?2024/12) because I was confused as fuck
    # (Up, Right), (Right, Down), (Down, Left), (Left, Up)
    directions = [
        ((-1, 0), (0, 1)),
        ((0, 1), (1, 0)),
        ((1, 0), (0, -1)),
        ((0, -1), (-1, 0)),
    ]
    corners = 0
    for elem in region:
        for du, dv in directions:
            if (elem[0] + du[0], elem[1] + du[1]) not in region and (
                elem[0] + dv[0],
                elem[1] + dv[1],
            ) not in region:
                corners += 1

            if (
                (elem[0] + du[0], elem[1] + du[1]) in region
                and (elem[0] + dv[0], elem[1] + dv[1]) in region
                and (elem[0] + du[0] + dv[0], elem[1] + du[1] + dv[1]) not in region
            ):
                corners += 1
    return corners


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 27.16 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 41.42 ms
