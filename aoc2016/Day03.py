import re
import time


def p1(data):
    return len([line for line in data if sum(sorted(line)[:2]) > max(line)])


def p2(data):
    t = 0
    for l1, l2, l3 in zip(data[0::3], data[1::3], data[2::3]):
        t += (
            1
            if sum(sorted([l1[0], l2[0], l3[0]])[:2]) > max([l1[0], l2[0], l3[0]])
            else 0
        )
        t += (
            1
            if sum(sorted([l1[1], l2[1], l3[1]])[:2]) > max([l1[1], l2[1], l3[1]])
            else 0
        )
        t += (
            1
            if sum(sorted([l1[2], l2[2], l3[2]])[:2]) > max([l1[2], l2[2], l3[2]])
            else 0
        )
    return t


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [list(map(int, re.split(r"\D+", line)[1:-1])) for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 731.23 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 997.30 μs
