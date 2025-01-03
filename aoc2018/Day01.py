import time


def p1(data):
    return sum(data)


def p2(data):
    seen = set()
    t = 0
    i = 0
    while t not in seen:
        seen.add(t)
        t += int(data[i])
        i = (i + 1) % len(data)
    return t


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [int(line.strip()) for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 137.33 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 18.09 ms
