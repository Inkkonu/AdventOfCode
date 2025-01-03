import time


def p1(data):
    dic = {
        "AY": 8,
        "AX": 4,
        "AZ": 3,
        "BY": 5,
        "BX": 1,
        "BZ": 9,
        "CY": 2,
        "CX": 7,
        "CZ": 6,
    }
    return sum([dic[line[0] + line[2]] for line in data])


def p2(data):
    dic = {
        "AY": 4,
        "AX": 3,
        "AZ": 8,
        "BY": 5,
        "BX": 1,
        "BZ": 9,
        "CY": 6,
        "CX": 2,
        "CZ": 7,
    }
    return sum([dic[line[0] + line[2]] for line in data])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 406.27 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 306.37 μs
