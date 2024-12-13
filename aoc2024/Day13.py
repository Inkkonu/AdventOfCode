from sympy import symbols, Eq, solve


def p1(data):
    total = 0
    for line in data:
        if line.startswith('Button A'):
            line = line.split(': ')[1].split(', ')
            x1 = int(line[0].split('+')[1])
            y1 = int(line[1].split('+')[1])
        elif line.startswith('Button B'):
            line = line.split(': ')[1].split(', ')
            x2 = int(line[0].split('+')[1])
            y2 = int(line[1].split('+')[1])
        elif line.startswith('Prize'):
            line = line.split(': ')[1].split(', ')
            xTotal = int(line[0].split('=')[1])
            yTotal = int(line[1].split('=')[1])

            a, b = symbols('a,b', integer=True, positive=True)
            eq1 = Eq((a*x1 + b*x2), xTotal)
            eq2 = Eq((a*y1 + b*y2), yTotal)

            s = solve((eq1, eq2), (a, b))
            if len(s) != 0:
                total += s[a] * 3 + s[b]
    return total


def p2(data):
    total = 0
    for line in data:
        if line.startswith('Button A'):
            line = line.split(': ')[1].split(', ')
            x1 = int(line[0].split('+')[1])
            y1 = int(line[1].split('+')[1])
        elif line.startswith('Button B'):
            line = line.split(': ')[1].split(', ')
            x2 = int(line[0].split('+')[1])
            y2 = int(line[1].split('+')[1])
        elif line.startswith('Prize'):
            line = line.split(': ')[1].split(', ')
            xTotal = int(line[0].split('=')[1]) + 10000000000000
            yTotal = int(line[1].split('=')[1]) + 10000000000000

            a, b = symbols('a,b', integer=True, positive=True)
            eq1 = Eq((a*x1 + b*x2), xTotal)
            eq2 = Eq((a*y1 + b*y2), yTotal)

            s = solve((eq1, eq2), (a, b))
            if len(s) != 0:
                total += s[a] * 3 + s[b]
    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')  # 1.26 second
    print(f'Part 2 : {p2(data)}')  # 1.20 second
