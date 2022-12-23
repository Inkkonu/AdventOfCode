def p1(data):
    d = dict()
    for e in data:
        if e in d.values():
            return e * (2020-e)
        d[e] = 2020-e


def p2(data):
    for i in range(len(data)-2):
        for j in range(i+1, len(data)-1):
            for k in range(j+1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
