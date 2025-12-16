import time


def p1(input):
    t = 0
    for x in input:
        x = x.split("-")
        l, u = int(x[0]), int(x[1])
        for i in range(l, u + 1):
            i = str(i)
            if len(i) % 2 == 0 and i[:len(i) // 2] == i[len(i) // 2:]:
                t += int(i)
    return t


def p2(input):
    t = 0
    for x in input:
        x = x.split("-")
        l, u = int(x[0]), int(x[1])
        for i in range(l, u + 1):
            i = str(i)
            for n in range(1, 1 + len(i) // 2):
                parts = [i[y:y + n] for y in range(0, len(i), n)]
                if len(set(parts)) == 1:
                    t += int(i)
                    break
    return t


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip().split(",") for line in f.readlines()][0]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 290.58 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 3.63s
