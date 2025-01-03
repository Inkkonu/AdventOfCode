import time


def p1(data):
    total = 0
    for line in data:
        total += 1 if isSafe(line) else 0
    return total


def p2(data):
    total = 0
    for line in data:
        if isSafe(line):
            total += 1
        else:
            safe = False
            for i in range(len(line)):
                if isSafe(line[:i] + line[i + 1 :]):
                    safe = True
            total += 1 if safe else 0
    return total


def isSafe(line):
    if line == sorted(line) or line == sorted(line, reverse=True):
        safe = True
        for i in range(len(line) - 1):
            if not 1 <= abs(line[i] - line[i + 1]) <= 3:
                safe = False
        return safe
    return False


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [list(map(int, line.strip().split())) for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 769.14 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 3.30 ms
