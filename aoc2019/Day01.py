import time


def p1(data):
    return sum([mass // 3 - 2 for mass in data])


def p2(data):
    total = 0
    for mass in data:
        total += mass // 3 - 2
        fuel = (mass // 3 - 2) // 3 - 2
        while fuel > 0:
            total += fuel
            fuel = fuel // 3 - 2
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [int(line.strip()) for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 323.77 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 226.97 μs
