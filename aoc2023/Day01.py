import re


def p1(data):
    total = 0
    for line in data:
        line = re.sub('\D', '', line)
        total += int(line[0] + line[-1])
    return total


def p2(data):
    total = 0
    for line in data:
        line = line.replace('one', 'o1e')
        line = line.replace('two', 't2o')
        line = line.replace('three', 'th3ee')
        line = line.replace('four', 'fo4ur')
        line = line.replace('five', 'fi5ve')
        line = line.replace('six', 's6x')
        line = line.replace('seven', 'se7en')
        line = line.replace('eight', 'ei8ht')
        line = line.replace('nine', 'ni9ne')
        line = re.sub('\D', '', line)
        total += int(line[0] + line[-1])
    return total


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
