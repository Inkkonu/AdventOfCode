import time
from functools import reduce


def p1(input):
    t = 0
    for i in range(len(input[0])):
        if input[-1][i] == "+":
            t += sum([int(input[j][i]) for j in range(len(input) - 1)])
        else:
            t += reduce(lambda x, y: x * y, [int(input[j][i]) for j in range(len(input) - 1)])
    return t


def p2(input):
    input = list(zip(*input))[::-1]
    #input.insert(0,
    #             ['4', '7', '7', ' ', ' '])  # Rotating my matrix makes the last column disappear so I readd it myself
    t = 0
    numbers = []
    for i in range(len(input)):
        if all([input[i][j] == " " for j in range(len(input[i]))]):
            numbers = []
            continue
        numbers.append(int("".join(input[i][:-1])))
        if input[i][-1] == "+":
            t += sum(numbers)
        elif input[i][-1] == "*":
            t += reduce(lambda x, y: x * y, numbers)
    return t


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
        for i, line in enumerate(data):
            data[i] = list(filter(lambda item: item, line.split(" ")))
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 0.64 ms
    with open("input.txt", "r") as f:
        data = [list(line.strip("\n")) for line in f.readlines()]
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 3.35 ms
