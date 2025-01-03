import time


def p1(data):
    i = 0
    while len(set(data[0][i : i + 4])) != 4:
        i += 1
    return i + 4


def p2(data):
    i = 0
    while len(set(data[0][i : i + 14])) != 14:
        i += 1
    return i + 14


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 494.96 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 1.33 ms
