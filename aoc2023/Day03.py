import collections
import time


def p1(data):
    total = 0
    for x in range(len(data)):
        currNumber = ""
        isNextToSymbol = False
        for y in range(len(data[1])):
            if data[x][y].isdigit():
                currNumber += data[x][y]

                for xx in [-1, 0, 1]:
                    for yy in [-1, 0, 1]:
                        try:
                            if data[x + xx][y + yy] != "." and not (
                                data[x + xx][y + yy].isdigit()
                            ):
                                isNextToSymbol = True
                        except IndexError:
                            continue

            if not data[x][y].isdigit() or y == len(data[1]) - 1:
                if isNextToSymbol:
                    total += int(currNumber)

                isNextToSymbol = False
                currNumber = ""
    return total


def p2(data):
    total = 0
    gears = collections.defaultdict(list)
    for x in range(len(data)):
        currNumber = ""
        gear = False
        for y in range(len(data[1])):
            if data[x][y].isdigit():
                currNumber += data[x][y]

                for xx in [-1, 0, 1]:
                    for yy in [-1, 0, 1]:
                        try:
                            if data[x + xx][y + yy] == "*":
                                gear = (x + xx, y + yy)
                        except IndexError:
                            continue

            if not data[x][y].isdigit() or y == len(data[1]) - 1:
                if gear:
                    gears[gear].append(int(currNumber))
                    if len(gears[gear]) == 2:
                        total += int(currNumber) * gears[gear][0]
                    gear = False
                currNumber = ""
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 3.41 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 3.21 ms
