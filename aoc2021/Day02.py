import time


def p1(data):
    x = depth = 0
    for line in data:
        parts = line.split(" ")
        instruc, n = parts[0], int(parts[1])
        if instruc == "forward":
            x += n
        elif instruc == "down":
            depth += n
        elif instruc == "up":
            depth -= n
    return x * depth


def p2(data):
    x = depth = aim = 0
    for line in data:
        parts = line.split(" ")
        instruc, n = parts[0], int(parts[1])
        if instruc == "forward":
            x += n
            depth += aim * n
        elif instruc == "down":
            aim += n
        elif instruc == "up":
            aim -= n
    return x * depth


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 335.93 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 245.09 μs
