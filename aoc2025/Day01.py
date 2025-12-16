import time


def p1(input):
    t = 50
    c = 0
    for v in input:
        d, x = v[0], int(v[1:])
        t += x if d == "R" else -x
        if t % 100 == 0:
            c += 1
    return c


def p2(input):
    t = 50
    c = 0
    for v in input:
        d, x = v[0], int(v[1:])
        for _ in range(x):
            t += 1 if d == "R" else -1
            if t % 100 == 0:
                c += 1
    return c


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 0.71 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 32.17 ms
