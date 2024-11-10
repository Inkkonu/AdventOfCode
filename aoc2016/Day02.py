def p1(data):
    code = ""
    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    x = y = 1
    for line in data:
        for d in line:
            if d == 'U':
                x -= 1
            elif d == 'D':
                x += 1
            elif d == 'R':
                y += 1
            elif d == 'L':
                y -= 1
            x = min(2, max(x, 0))
            y = min(2, max(y, 0))
        code += keypad[x][y]
    return code


def p2(data):
    code = ""
    keypad = [[None, None, '1', None, None], [None, '2', '3', '4', None], ['5', '6', '7', '8', '9'],
              [None, 'A', 'B', 'C', None], [None, None, 'D', None, None]]
    x = 2
    y = 0
    for line in data:
        for d in line:
            if d == 'U':
                x -= 1
                if x < 0 or keypad[x][y] is None:
                    x += 1
            elif d == 'D':
                x += 1
                if x > 4 or keypad[x][y] is None:
                    x -= 1
            elif d == 'R':
                y += 1
                if y > 4 or keypad[x][y] is None:
                    y -= 1
            elif d == 'L':
                y -= 1
                if y < 0 or keypad[x][y] is None:
                    y += 1
        code += keypad[x][y]
    return code


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
