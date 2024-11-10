def p1(data):
    times = [int(x) for x in data[0].split()[1:]]
    distances = [int(x) for x in data[1].split()[1:]]  # Use zip()

    total = 1
    for time, distance in zip(times, distances):
        n = 0
        for i in range(1, time):
            t = i * (time - i)
            if t > distance:
                n += 1
        total *= n
    return total


def p2(data):
    time = int(''.join(data[0].split()[1:]))
    distance = int(''.join(data[1].split()[1:]))

    total = 0
    for i in range(1, time):
        t = i * (time - i)
        if t > distance:
            total += 1
    return total


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
