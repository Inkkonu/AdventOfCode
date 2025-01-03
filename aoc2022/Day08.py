import time


def p1(data):
    total = 0
    total += len(data) * 2
    total += len(data[0]) * 2 - 4
    for i, line in enumerate(data[1:-1]):
        for j, t in enumerate(line[1:-1]):
            if (
                all(t > e for e in line[: j + 1])
                or all(t > e for e in line[j + 2 :])
                or all(t > e for e in [row[j + 1] for row in data[: i + 1]])
                or all(t > e for e in [row[j + 1] for row in data[i + 2 :]])
            ):
                total += 1
    return total


def p2(data):
    max = 0
    for i, line in enumerate(data[1:-1]):
        for j, t in enumerate(line[1:-1]):
            left, right, up, down = (
                [t > e for e in line[: j + 1]][::-1],
                [t > e for e in line[j + 2 :]],
                [t > e for e in [row[j + 1] for row in data[: i + 1]]][::-1],
                [t > e for e in [row[j + 1] for row in data[i + 2 :]]],
            )
            count_left, count_right, count_up, count_down = 0, 0, 0, 0
            for b in left:
                if b:
                    count_left += 1
                else:
                    count_left += 1
                    break
            for b in right:
                if b:
                    count_right += 1
                else:
                    count_right += 1
                    break
            for b in up:
                if b:
                    count_up += 1
                else:
                    count_up += 1
                    break
            for b in down:
                if b:
                    count_down += 1
                else:
                    count_down += 1
                    break
            if count_left * count_right * count_up * count_down > max:
                max = count_left * count_right * count_up * count_down
    return max


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 34.60 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 78.71 ms
