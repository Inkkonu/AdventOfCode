import time


def p1(input):
    t = 0
    for x, line in enumerate(input):
        for y, p in enumerate(line):
            c = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (not (i == 0 and j == 0)) and 0 <= x + i < len(input) and 0 <= y + j < len(line):
                        if input[x + i][y + j] == "@":
                            c += 1
            if c < 4 and p == "@":
                t += 1
    return t


def p2(input):
    t = 0
    keep_going = False
    for x, line in enumerate(input):
        for y, p in enumerate(line):
            c = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (not (i == 0 and j == 0)) and 0 <= x + i < len(input) and 0 <= y + j < len(line):
                        if input[x + i][y + j] == "@":
                            c += 1
            if c < 4 and p == "@":
                input[x] = input[x][:y] + "." + input[x][y + 1:]
                keep_going = True
                t += 1
    if keep_going:
        return t + p2(input)
    return t


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 18.89 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 658.76 ms
