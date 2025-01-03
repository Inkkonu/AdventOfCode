import hashlib
import time


def p1(data):
    i = 0
    while True:
        if (
            hashlib.md5((data[0] + str(i)).encode("utf-8"))
            .hexdigest()
            .startswith("00000")
        ):
            return i
        i += 1


def p2(data):
    i = 0
    while True:
        if (
            hashlib.md5((data[0] + str(i)).encode("utf-8"))
            .hexdigest()
            .startswith("000000")
        ):
            return i
        i += 1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 244.19 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 6.79 s
