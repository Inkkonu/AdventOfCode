from functools import cache
from math import floor, log10
from collections import Counter


def p1(data):
    return loop(data, 25)


def p2(data):
    return loop(data, 75)


def loop(data, n):
    counter = Counter(data)

    for _ in range(n):
        newCounter = Counter()

        for stone, count in counter.items():
            result = blink(stone)
            for new_stone in result:
                newCounter[new_stone] += count
        counter = newCounter
    return sum(counter.values())


@cache  # Gains 0.02 second for part 2, nothing for part 1
def blink(n):
    if n == 0:
        return [1]
    digits = floor(log10(n)) + 1
    if (digits & 1) == 0:  # If the numbers of digits is even
        divisor = 10 ** (digits // 2)
        return [n//divisor, n % divisor]  # Split the number in half
    return [n*2024]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [list(map(int, line.strip().split(' ')))
                for line in f.readlines()][0]
    print(f'Part 1 : {p1(data)}')  # 0.002 second
    print(f'Part 2 : {p2(data)}')  # 0.05 second
