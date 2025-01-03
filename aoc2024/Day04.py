import time


def p1(data):
    total = 0
    word = "XMAS"
    dirX = [-1, -1, -1, 0, 0, 1, 1, 1]
    dirY = [-1, 0, 1, -1, 1, -1, 0, 1]
    for x, line in enumerate(data):
        for y, c in enumerate(line):
            for i in range(8):
                if findWord(word, data, x, y, (dirX[i], dirY[i])):
                    total += 1
    return total


def findWord(word, data, x, y, direction):
    if len(word) == 1 and data[x][y] == word[0]:
        return True
    if data[x][y] == word[0]:
        found = False
        if 0 <= x + direction[0] < len(data) and 0 <= y + direction[1] < len(data[0]):
            found |= findWord(
                word[1:], data, x + direction[0], y + direction[1], direction
            )
        return found
    return False


def p2(data):
    total = 0
    for x, line in enumerate(data):
        for y, c in enumerate(line):
            if x != 0 and y != 0 and x != len(data) - 1 and y != len(line) - 1:
                if c == "A":
                    if (data[x - 1][y - 1] == "S" and data[x + 1][y + 1] == "M") or (
                        data[x - 1][y - 1] == "M" and data[x + 1][y + 1] == "S"
                    ):
                        if (
                            data[x - 1][y + 1] == "S" and data[x + 1][y - 1] == "M"
                        ) or (data[x - 1][y + 1] == "M" and data[x + 1][y - 1] == "S"):
                            total += 1
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 26.63 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 2.18 ms
