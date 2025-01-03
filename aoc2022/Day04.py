import time


def p1(data):
    t = 0
    for line in data:
        e1, e2 = line.split(",")[0], line.split(",")[1]
        s1, s2 = (
            {i for i in range(int(e1.split("-")[0]), int(e1.split("-")[1]) + 1)},
            {i for i in range(int(e2.split("-")[0]), int(e2.split("-")[1]) + 1)},
        )
        if s1.issubset(s2) or s2.issubset(s1):
            t += 1
    return t


def p2(data):
    t = 0
    for line in data:
        e1, e2 = line.split(",")[0], line.split(",")[1]
        s1, s2 = (
            {i for i in range(int(e1.split("-")[0]), int(e1.split("-")[1]) + 1)},
            {i for i in range(int(e2.split("-")[0]), int(e2.split("-")[1]) + 1)},
        )
        if len(s1.intersection(s2)) != 0:
            t += 1
    return t


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 2.58 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 2.78 ms
