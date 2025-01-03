import math
import time


def p1(data):
    total = 0
    for line in data:
        line = line.split("|")
        line[0] = line[0].split(":")[1]
        winning = set(map(int, [x for x in line[0].split(" ") if x]))
        myNumbers = set(map(int, [x for x in line[1].split(" ") if x]))
        total += math.floor(2 ** (len(winning.intersection(myNumbers)) - 1))
    return total


def p2(data):
    d = {i: 1 for i in range(1, len(data) + 1)}
    for i, line in enumerate(data[:-1]):
        line = line.split("|")
        line[0] = line[0].split(":")[1]
        winning = set(map(int, [x for x in line[0].split(" ") if x]))
        myNumbers = set(map(int, [x for x in line[1].split(" ") if x]))
        n = len(winning.intersection(myNumbers))
        for j in range(n):
            d[i + j + 2] += d[i + 1]
    return sum(d.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 1.31 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 1.32 ms
