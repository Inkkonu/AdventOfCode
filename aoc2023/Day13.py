import time


def findSymmetry(pattern, rotated):
    for i, line in enumerate(pattern[:-1]):
        if line == pattern[i + 1]:
            if i < len(pattern) // 2:
                if pattern[: i + 1] == pattern[i + 1 : i + i + 2][::-1]:
                    return (i + 1) * 100 if not rotated else i + 1
            else:
                p = pattern[i + 1 :]
                if pattern[i - len(p) + 1 : i + 1] == p[::-1]:
                    return (i + 1) * 100 if not rotated else i + 1
    return findSymmetry(list(zip(*pattern)), not rotated)


def hammingDistance(l1, l2):
    return sum([0 if v1 == v2 else 1 for v1, v2 in zip(l1, l2)])


def findSymmetryUsingHammingDistance(pattern, rotated):
    for i, line in enumerate(pattern[:-1]):
        if line == pattern[i + 1] or hammingDistance(line, pattern[i + 1]) == 1:
            if i < len(pattern) // 2:
                patt1, patt2 = pattern[: i + 1], pattern[i + 1 : i + i + 2][::-1]
            else:
                p = pattern[i + 1 :]
                patt1, patt2 = pattern[i - len(p) + 1 : i + 1], p[::-1]

            hamming = 0
            for l1, l2 in zip(patt1, patt2):
                hamming += hammingDistance(l1, l2)
            if hamming == 1:
                return (i + 1) * 100 if not rotated else i + 1
    return findSymmetryUsingHammingDistance(list(zip(*pattern)), not rotated)


def p1(data):
    pattern = []
    total = 0
    for line in data:
        if line:
            pattern.append(line)
        else:
            total += findSymmetry(pattern, False)
            pattern = []
    return total


def p2(data):
    pattern = []
    total = 0
    for line in data:
        if line:
            pattern.append(line)
        else:
            total += findSymmetryUsingHammingDistance(pattern, False)
            pattern = []
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 397.21 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 1.47 ms
