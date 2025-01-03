import time
from collections import Counter


def p1(data):
    l1 = sorted(data[0])
    l2 = sorted(data[1])
    total = 0
    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])
    return total


def p2(data):
    c = Counter(data[1])
    total = 0
    for n in data[0]:
        total += n * c[n]
    return total


if __name__ == "__main__":
    data = []
    l1, l2 = [], []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            line = line.split()
            l1.append(int(line[0]))
            l2.append(int(line[1]))
    data = [l1, l2]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 355.96 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 274.18 μs
