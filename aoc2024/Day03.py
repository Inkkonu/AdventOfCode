import re


def p1(data):
    total = 0
    for line in data:
        muls = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        for mul in muls:
            mul = mul.split(",")
            x, y = int(mul[0][4:]), int(mul[1][:-1])
            total += x*y
    return total


def p2(data):
    total = 0
    for line in data:
        dos = re.findall("do\(\).*?don't\(\)", line)
        for do in dos:
            muls = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", do)
            for mul in muls:
                mul = mul.split(",")
                x, y = int(mul[0][4:]), int(mul[1][:-1])
                total += x*y
    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        # But you need to change the AoC's input to have it on one line, else it adds undesired do() and don't()
        data = ["do()" + line.strip() + "don't()" for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
