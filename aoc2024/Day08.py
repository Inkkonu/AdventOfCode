import time
from collections import defaultdict


def p1(data):
    antinodes = set()
    antennas = defaultdict(list)
    for x, line in enumerate(data):
        for y, v in enumerate(line):
            if v != ".":
                antennas[v].append((x, y))
    for type in antennas.keys():
        antennasOfType = antennas[type]
        for i in range(len(antennasOfType) - 1):
            for j in range(i + 1, len(antennasOfType)):
                xDiff = antennasOfType[i][0] - antennasOfType[j][0]
                yDiff = antennasOfType[i][1] - antennasOfType[j][1]
                antinodesX = antennasOfType[i][0] + xDiff
                antinodesY = antennasOfType[i][1] + yDiff
                if (
                    0 <= antinodesX <= len(data) - 1
                    and 0 <= antinodesY <= len(data[0]) - 1
                ):
                    antinodes.add((antinodesX, antinodesY))

                xDiff = antennasOfType[j][0] - antennasOfType[i][0]
                yDiff = antennasOfType[j][1] - antennasOfType[i][1]
                antinodesX = antennasOfType[j][0] + xDiff
                antinodesY = antennasOfType[j][1] + yDiff
                if (
                    0 <= antinodesX <= len(data) - 1
                    and 0 <= antinodesY <= len(data[0]) - 1
                ):
                    antinodes.add((antinodesX, antinodesY))

    return len(antinodes)


def p2(data):
    antinodes = set()
    antennas = defaultdict(list)
    for x, line in enumerate(data):
        for y, v in enumerate(line):
            if v != ".":
                antennas[v].append((x, y))
    for type in antennas.keys():
        antennasOfType = antennas[type]
        for i in range(len(antennasOfType) - 1):
            for j in range(i + 1, len(antennasOfType)):
                xDiff = antennasOfType[i][0] - antennasOfType[j][0]
                yDiff = antennasOfType[i][1] - antennasOfType[j][1]
                antinodesX = antennasOfType[i][0]
                antinodesY = antennasOfType[i][1]
                while (
                    0 <= antinodesX <= len(data) - 1
                    and 0 <= antinodesY <= len(data[0]) - 1
                ):
                    antinodes.add((antinodesX, antinodesY))
                    antinodesX += xDiff
                    antinodesY += yDiff

                xDiff = antennasOfType[j][0] - antennasOfType[i][0]
                yDiff = antennasOfType[j][1] - antennasOfType[i][1]
                antinodesX = antennasOfType[j][0]
                antinodesY = antennasOfType[j][1]
                while (
                    0 <= antinodesX <= len(data) - 1
                    and 0 <= antinodesY <= len(data[0]) - 1
                ):
                    antinodes.add((antinodesX, antinodesY))
                    antinodesX += xDiff
                    antinodesY += yDiff

    return len(antinodes)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 394.11 μs
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 641.58 μs
