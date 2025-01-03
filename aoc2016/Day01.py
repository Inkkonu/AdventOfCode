import time


def p1(data):
    x = y = 0
    directions = ["N", "E", "S", "W"]
    direction = 0
    for i in data:
        direction += 1 if i[0] == "R" else -1
        if directions[direction % 4] == "N":
            y += int(i[1:])
        elif directions[direction % 4] == "E":
            x += int(i[1:])
        elif directions[direction % 4] == "S":
            y -= int(i[1:])
        elif directions[direction % 4] == "W":
            x -= int(i[1:])
    return abs(x) + abs(y)


def p2(data):
    x = y = 0
    seen = set()
    directions = ["N", "E", "S", "W"]
    direction = 0
    for i in data:
        direction += 1 if i[0] == "R" else -1
        if directions[direction % 4] == "N":
            for j in range(int(i[1:])):
                y += 1
                if (x, y) in seen:
                    return abs(x) + abs(y)
                seen.add((x, y))
        elif directions[direction % 4] == "E":
            for j in range(int(i[1:])):
                x += 1
                if (x, y) in seen:
                    return abs(x) + abs(y)
                seen.add((x, y))
        elif directions[direction % 4] == "S":
            for j in range(int(i[1:])):
                y -= 1
                if (x, y) in seen:
                    return abs(x) + abs(y)
                seen.add((x, y))
        elif directions[direction % 4] == "W":
            for j in range(int(i[1:])):
                x -= 1
                if (x, y) in seen:
                    return abs(x) + abs(y)
                seen.add((x, y))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip().split(",") for line in f.readlines()][0]
        data = [data[0]] + [s[1:] for s in data[1:]]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 175.48 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 180.72 μs
