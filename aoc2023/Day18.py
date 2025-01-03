import time


def p1(data):  # Check out Shoelace Formula and Pick's theorem
    area = perimeter = x = y = 0
    for line in data:
        line = line.split()
        d, v = line[0], int(line[1])
        perimeter += v
        if d == "U":
            area += (x * y) - ((x - v) * y)
            x -= v
        elif d == "D":
            area += (x * y) - ((x + v) * y)
            x += v
        elif d == "R":
            area += (x * (y + v)) - (x * y)
            y += v
        elif d == "L":
            area += (x * (y - v)) - (x * y)
            y -= v
    area = abs(area // 2)
    pointsInside = area - perimeter // 2 + 1
    return pointsInside + perimeter


def p2(data):
    area = perimeter = x = y = 0
    for line in data:
        color = line.split()[-1][1:-1]
        directions = ["R", "D", "L", "U"]
        d = directions[int(color[-1])]
        v = int(color[1:-1], 16)
        perimeter += v
        if d == "U":
            area += (x * y) - ((x - v) * y)
            x -= v
        elif d == "D":
            area += (x * y) - ((x + v) * y)
            x += v
        elif d == "R":
            area += (x * (y + v)) - (x * y)
            y += v
        elif d == "L":
            area += (x * (y - v)) - (x * y)
            y -= v
    area = abs(area // 2)
    pointsInside = area - perimeter // 2 + 1
    return pointsInside + perimeter


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 337.36 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 532.63 μs
