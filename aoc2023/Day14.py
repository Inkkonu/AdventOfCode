def p1(data):
    data = list(map(list, list(zip(*data))))
    for i, line in enumerate(data):
        for k in range(len(line[:-1])):
            j = k
            while j >= 0 and line[j + 1] == 'O' and line[j] == '.':
                line[j], line[j + 1] = line[j + 1], line[j]
                j -= 1

    data = list(zip(*data))

    total = 0
    for i in range(len(data)):
        total += data[i].count('O') * (len(data) - i)
    return total



def p2(data):
    return None


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
