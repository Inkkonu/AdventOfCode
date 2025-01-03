import time


def p1(data):
    return sum([1 if data[i] > data[i - 1] else 0 for i in range(len(data))])


def p2(data):
    return sum(
        [
            1 if sum(data[i : i + 3]) > sum(data[i - 1 : i - 1 + 3]) else 0
            for i in range(1, len(data))
        ]
    )


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [int(line.strip()) for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 269.41 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 658.51 μs
