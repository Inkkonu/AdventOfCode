import time


def p1(data):
    return sum([1 if c == "(" else -1 for c in data[0]])


def p2(data):
    floor = 0
    for i, c in enumerate(data[0]):
        floor += 1 if c == "(" else -1
        if floor == -1:
            return i + 1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 486.14 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 185.72 μs
