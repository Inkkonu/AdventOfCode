import time


def p1(ranges, ingredients):
    t = 0
    for ingredient in ingredients:
        if any([mini <= int(ingredient) <= maxi for r in ranges for mini, maxi in [map(int, r.split("-"))]]):
            t += 1
    return t


# Written by Copilot because fuck maths of intervals
def p2(ranges):
    # parse intervals
    intervals = sorted((min(int(a), int(b)), max(int(a), int(b))) for r in ranges for a, b in [r.split("-")])
    # merge
    merged = []
    for a, b in intervals:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)
    # sum sizes (inclusive)
    return sum(b - a + 1 for a, b in merged)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
        i = data.index("")
        ranges = data[:i]
        ingredients = data[i + 1:]
    start = time.time()
    print(f"Part 1 : {p1(ranges, ingredients)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 64.56 ms
    start = time.time()
    print(f"Part 2 : {p2(ranges)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 0.15 ms
