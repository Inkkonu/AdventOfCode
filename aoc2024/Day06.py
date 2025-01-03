import time


def p1(data):
    startX = startY = -1
    seen = set()
    direction = "^"
    for x, line in enumerate(data):
        for y, v in enumerate(line):
            if v == "^":
                startX, startY = x, y
                seen.add((x, y))
    while not (
        (startX == 0 and direction == "^")
        or (startX == len(data) - 1 and direction == "v")
        or (startY == 0 and direction == "<")
        or (startY == len(data[0]) - 1 and direction == ">")
    ):
        if direction == "^":
            if data[startX - 1][startY] == "#":
                direction = ">"
            else:
                startX -= 1
                seen.add((startX, startY))
        elif direction == ">":
            if data[startX][startY + 1] == "#":
                direction = "v"
            else:
                startY += 1
                seen.add((startX, startY))
        elif direction == "v":
            if data[startX + 1][startY] == "#":
                direction = "<"
            else:
                startX += 1
                seen.add((startX, startY))
        elif direction == "<":
            if data[startX][startY - 1] == "#":
                direction = "^"
            else:
                startY -= 1
                seen.add((startX, startY))
    return len(seen)


def p2(data):
    startX = startY = -1
    direction = "^"
    for x, line in enumerate(data):
        for y, v in enumerate(line):
            if v == direction:
                startX, startY = x, y
    seen = doPath(data, startX, startY, direction)[0]
    worked = set()
    for pos in seen:
        x, y = pos[0], pos[1]
        if x != startX or y != startY:
            modifyString = list(data[x])
            modifyString[y] = "#"
            data[x] = "".join(modifyString)
            if doPath(data, startX, startY, direction)[1]:
                worked.add((x, y))
            modifyString = list(data[x])
            modifyString[y] = "."
            data[x] = "".join(modifyString)
    return len(worked)


def doPath(data, startX, startY, direction):
    seen = {(startX, startY, direction)}
    while not (
        (startX == 0 and direction == "^")
        or (startX == len(data) - 1 and direction == "v")
        or (startY == 0 and direction == "<")
        or (startY == len(data[0]) - 1 and direction == ">")
    ):
        if direction == "^":
            if data[startX - 1][startY] == "#":
                direction = ">"
            else:
                startX -= 1
                if (startX, startY, direction) in seen:
                    return seen, True
                seen.add((startX, startY, direction))
        elif direction == ">":
            if data[startX][startY + 1] == "#":
                direction = "v"
            else:
                startY += 1
                if (startX, startY, direction) in seen:
                    return seen, True
                seen.add((startX, startY, direction))
        elif direction == "v":
            if data[startX + 1][startY] == "#":
                direction = "<"
            else:
                startX += 1
                if (startX, startY, direction) in seen:
                    return seen, True
                seen.add((startX, startY, direction))
        elif direction == "<":
            if data[startX][startY - 1] == "#":
                direction = "^"
            else:
                startY -= 1
                if (startX, startY, direction) in seen:
                    return seen, True
                seen.add((startX, startY, direction))
    return (seen, False)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 1.64 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 3.38 s
