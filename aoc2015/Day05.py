import time


def p1(data):
    t = 0
    for line in data:
        if not any(seq in line for seq in ["ab", "cd", "pq", "xy"]):
            d = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
            doubleletters = False
            i = 0
            for i in range(len(line) - 1):
                if line[i] in d:
                    d[line[i]] += 1
                if not doubleletters and line[i] == line[i + 1]:
                    doubleletters = True
            if line[i + 1] in d:
                d[line[i + 1]] += 1
            if sum([d[k] for k in d]) >= 3 and doubleletters:
                t += 1
    return t


def p2(data):
    t = 0
    for line in data:
        pair = False
        soloRepeat = False
        for i in range(len(line) - 2):
            if not soloRepeat and line[i] == line[i + 2]:
                soloRepeat = True
            if not pair and line[i] + line[i + 1] in line[i + 2 :]:
                pair = True
        if pair and soloRepeat:
            t += 1
    return t


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 2.00 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 1.93 s
