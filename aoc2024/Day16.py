import time
from heapq import heappop, heappush


def p1(data):
    # Big inspiration from here : https://github.com/mgtezak/Advent_of_Code/blob/master/2024/16/p1.py
    for x, line in enumerate(data):
        for y, v in enumerate(line):
            if v == "S":
                start = (x, y)
                break

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    heap = [(0, 0, *start)]
    visited = set()
    while heap:
        score, direction, x, y = heappop(heap)
        if data[x][y] == "E":
            break

        if (direction, x, y) in visited:
            continue

        visited.add((direction, x, y))

        newX = x + directions[direction][0]
        newY = y + directions[direction][1]
        if data[newX][newY] != "#" and (direction, newX, newY) not in visited:
            heappush(heap, (score + 1, direction, newX, newY))

        left = (direction - 1) % 4
        newX = x + directions[left][0]
        newY = y + directions[left][1]
        if data[newX][newY] != "#" and (left, newX, newY) not in visited:
            heappush(heap, (score + 1001, left, newX, newY))

        right = (direction + 1) % 4
        newX = x + directions[right][0]
        newY = y + directions[right][1]
        if data[newX][newY] != "#" and (right, newX, newY) not in visited:
            heappush(heap, (score + 1001, right, newX, newY))

    return score


def p2(data):
    return 0


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 13.477 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  #
