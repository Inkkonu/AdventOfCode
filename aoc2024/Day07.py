import time
from itertools import product


def p1(data):
    total = 0
    for line in data:
        line = line.split(":")
        goal, numbers = int(line[0]), list(map(int, line[1].split(" ")[1:]))
        combinations = product(["+", "*"], repeat=len(numbers) - 1)
        for combination in combinations:
            if evaluate_expression(numbers, combination) == goal:
                total += goal
                break
    return total


def evaluate_expression(numbers, operators):
    total = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            total += numbers[i + 1]
        elif op == "*":
            total *= numbers[i + 1]
        elif op == "||":
            total = int(str(total) + str(numbers[i + 1]))
    return total


def p2(data):
    total = 0
    for line in data:
        line = line.split(":")
        goal, numbers = int(line[0]), list(map(int, line[1].split(" ")[1:]))
        combinations = product(["+", "*", "||"], repeat=len(numbers) - 1)
        for combination in combinations:
            if evaluate_expression(numbers, combination) == goal:
                total += goal
                break
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 149.75 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 12.21 s
