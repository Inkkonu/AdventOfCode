import time
from collections import Counter


def p1(data):
    two_letters = three_letters = 0
    for line in data:
        d = Counter(line)
        if 2 in d.values():
            two_letters += 1
        if 3 in d.values():
            three_letters += 1
    return two_letters * three_letters


def p2(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if sum(1 for a, b in zip(data[i], data[j]) if a != b) == 1:
                k = 0
                while data[i][k] == data[j][k]:
                    k += 1
                return data[i][:k] + data[i][k + 1 :]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 712.39 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 10.39 ms
