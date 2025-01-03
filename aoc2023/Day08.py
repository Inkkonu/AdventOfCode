import math
import time


def p1(data):
    network = {}
    instructions = data[0].replace("L", "0").replace("R", "1")
    for line in data[2:]:
        line = line.split("=")
        key = line[0][:-1]
        line[1] = line[1].split()
        left, right = line[1][0][1:-1], line[1][1][:-1]
        network[key] = (left, right)
    current = "AAA"
    counter = 0
    while current != "ZZZ":
        current = network[current][int(instructions[counter % len(instructions)])]
        counter += 1
    return counter


def p2(data):
    network = {}
    instructions = data[0].replace("L", "0").replace("R", "1")
    for line in data[2:]:
        line = line.split("=")
        key = line[0][:-1]
        line[1] = line[1].split()
        left, right = line[1][0][1:-1], line[1][1][:-1]
        network[key] = (left, right)

    currents = list(filter(lambda x: x[-1] == "A", network.keys()))
    numberOfSteps = []
    for current in currents:
        counter = 0
        while current[-1] != "Z":
            current = network[current][int(instructions[counter % len(instructions)])]
            counter += 1
        numberOfSteps.append(counter)
    return math.lcm(*numberOfSteps)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 2.70 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 15.90 ms
