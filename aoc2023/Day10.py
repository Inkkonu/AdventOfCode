import time


def p1(data):
    def followPath(x, y, dist, d, comeFrom):
        while (x, y) != s:
            dist += 1
            d[(x, y)] = dist
            if data[x][y] == "|":
                if comeFrom == "TOP":
                    x += 1
                else:
                    x += -1
            elif data[x][y] == "-":
                if comeFrom == "LEFT":
                    y += 1
                else:
                    y += -1
            elif data[x][y] == "L":
                if comeFrom == "TOP":
                    y += 1
                    comeFrom = "LEFT"
                else:
                    x += -1
                    comeFrom = "BOTTOM"
            elif data[x][y] == "J":
                if comeFrom == "TOP":
                    y += -1
                    comeFrom = "RIGHT"
                else:
                    x += -1
                    comeFrom = "BOTTOM"
            elif data[x][y] == "7":
                if comeFrom == "BOTTOM":
                    y += -1
                    comeFrom = "RIGHT"
                else:
                    x += 1
                    comeFrom = "TOP"
            elif data[x][y] == "F":
                if comeFrom == "BOTTOM":
                    y += 1
                    comeFrom = "LEFT"
                else:
                    x += 1
                    comeFrom = "TOP"
        return d

    s = (-1, -1)
    for i, line in enumerate(data):
        try:
            s = (i, line.index("S"))
        except ValueError:
            continue
    d1 = {}
    d2 = {}
    dist = 0
    comeFrom = ""
    d1[s] = dist
    d2[s] = dist
    x, y = s
    if data[x][y + 1] in ("J", "7", "-"):  # Look on the right
        y = y + 1
        comeFrom = "LEFT"
    elif data[x][y - 1] in ("L", "F", "-"):  # Look on the left
        y = y - 1
        comeFrom = "RIGHT"
    elif data[x - 1][y] in ("7", "F", "|"):  # Look on top
        x = x - 1
        comeFrom = "BOTTOM"
    elif data[x + 1][y] in ("L", "J", "|"):  # Look on bottom
        x = x + 1
        comeFrom = "TOP"
    d1 = followPath(x, y, dist, d1, comeFrom)

    x, y = s
    dist = 0
    if data[x + 1][y] in ("L", "J", "|"):  # Look on bottom
        x = x + 1
        comeFrom = "TOP"
    elif data[x - 1][y] in ("7", "F", "|"):  # Look on top
        x = x - 1
        comeFrom = "BOTTOM"
    elif data[x][y - 1] in ("L", "F", "-"):  # Look on the left
        y = y - 1
        comeFrom = "RIGHT"
    elif data[x][y + 1] in ("J", "7", "-"):  # Look on the right
        y = y + 1
        comeFrom = "LEFT"

    d2 = followPath(x, y, dist, d2, comeFrom)
    d = {key: min(d1[key], d2[key]) for key in d1.keys()}
    return max(d.values())


def p2(data):
    def followPath(x, y, d, comeFrom):
        while (x, y) != s:
            d.add((x, y))
            if data[x][y] == "|":
                if comeFrom == "TOP":
                    x += 1
                else:
                    x += -1
            elif data[x][y] == "-":
                if comeFrom == "LEFT":
                    y += 1
                else:
                    y += -1
            elif data[x][y] == "L":
                if comeFrom == "TOP":
                    y += 1
                    comeFrom = "LEFT"
                else:
                    x += -1
                    comeFrom = "BOTTOM"
            elif data[x][y] == "J":
                if comeFrom == "TOP":
                    y += -1
                    comeFrom = "RIGHT"
                else:
                    x += -1
                    comeFrom = "BOTTOM"
            elif data[x][y] == "7":
                if comeFrom == "BOTTOM":
                    y += -1
                    comeFrom = "RIGHT"
                else:
                    x += 1
                    comeFrom = "TOP"
            elif data[x][y] == "F":
                if comeFrom == "BOTTOM":
                    y += 1
                    comeFrom = "LEFT"
                else:
                    x += 1
                    comeFrom = "TOP"
        return d

    s = (-1, -1)
    for i, line in enumerate(data):
        try:
            s = (i, line.index("S"))
        except ValueError:
            continue
    d1 = set()
    comeFrom = ""
    d1.add(s)
    x, y = s
    if data[x][y + 1] in ("J", "7", "-"):  # Look on the right
        y = y + 1
        comeFrom = "LEFT"
    elif data[x][y - 1] in ("L", "F", "-"):  # Look on the left
        y = y - 1
        comeFrom = "RIGHT"
    elif data[x - 1][y] in ("7", "F", "|"):  # Look on top
        x = x - 1
        comeFrom = "BOTTOM"
    elif data[x + 1][y] in ("L", "J", "|"):  # Look on bottom
        x = x + 1
        comeFrom = "TOP"
    d1 = followPath(x, y, d1, comeFrom)

    tilesInLoop = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            numberOfIntersections = 0
            if (x, y) not in d1:
                for k in range(x):
                    if (k, y) in d1 and data[k][y] in (
                        "-",
                        "J",
                        "7",
                    ):  # My S is equivalent to a F
                        numberOfIntersections += 1
            if numberOfIntersections % 2 == 1:
                tilesInLoop += 1
    return tilesInLoop


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 10.07 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 31.40 ms
