import time


def p1(data):
    total = 0
    for line in data:
        line = [int(x) for x in line.split()]
        l = [line]
        while any(l[-1]):
            ll = [l[-1][i + 1] - l[-1][i] for i in range(len(l[-1]) - 1)]
            l.append(ll)
        l[-1].append(0)
        for i in range(len(l) - 2, -1, -1):
            l[i].append(l[i][-1] + l[i + 1][-1])
        total += l[0][-1]
    return total


def p2(data):
    total = 0
    for line in data:
        line = [int(x) for x in line.split()]
        l = [line]
        while any(l[-1]):
            ll = [l[-1][i + 1] - l[-1][i] for i in range(len(l[-1]) - 1)]
            l.append(ll)
        l[-1].insert(0, 0)
        for i in range(len(l) - 2, -1, -1):
            l[i].insert(0, l[i][0] - l[i + 1][0])
        total += l[0][0]
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 2.68 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 2.50 ms
