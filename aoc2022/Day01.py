import time


def p1(data):
    return data[-1]


def p2(data):
    return sum(data[-3:])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [""] + [
            int(line.strip()) if line.strip() != "" else "" for line in f.readlines()
        ]
        x = [i for i, s in enumerate(data) if s == ""]
        y = x[1:] + [len(data)]
        data = sorted(list(map(sum, [data[i + 1 : j] for i, j in zip(x, y)])))
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 133.04 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 52.45 μs
