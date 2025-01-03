import time


def p1(data):
    d = dict()
    cycle = x = 1
    for line in data:
        if line == "noop":
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                d[cycle] = x
        else:
            v = int(line.split(" ")[1])
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                d[cycle] = x
            cycle += 1
            x += v
            if cycle in {20, 60, 100, 140, 180, 220}:
                d[cycle] = x
    return sum([k * d[k] for k in d])


def p2(data):
    crt = [[" " for _ in range(40)] for _ in range(6)]
    cycle = x = 1
    for line in data:
        if line == "noop":
            if x - 1 <= (cycle - 1) % 40 <= x + 1:
                crt[cycle // 40][(cycle - 1) % 40] = "#"
            cycle += 1
        else:
            v = int(line.split(" ")[1])
            if x - 1 <= (cycle - 1) % 40 <= x + 1:
                crt[cycle // 40][(cycle - 1) % 40] = "#"
            cycle += 1
            if x - 1 <= (cycle - 1) % 40 <= x + 1:
                crt[cycle // 40][(cycle - 1) % 40] = "#"
            cycle += 1
            x += v

    s = "\n"
    for line in crt:
        s += " ".join(map(str, line)) + "\n"
    return s


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 92.74 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 150.44 μs
