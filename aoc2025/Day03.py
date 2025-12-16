import time


def p1(input):
    t = 0
    for line in input:
        maxi = max(line[:-1])
        i = line.index(maxi)
        line = line[i + 1:]
        maxi2 = max(line)
        t += int(maxi + maxi2)
    return t


def p2(input):
    t = 0
    for line in input:
        v = ""
        for i in range(11, 0, -1):
            maxi = max(line[:-i])
            i = line.index(maxi)
            line = line[i + 1:]
            v += maxi
        maxi = max(line)
        v += maxi
        t += int(v)
    return t


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 0.38 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 1.023 ms
