def p1():
    # From https://stackoverflow.com/a/36889800
    NORTH, S, W, E = (0, 1), (0, -1), (-1, 0), (1, 0)  # directions
    turn_right = {NORTH: E, E: S, S: W, W: NORTH}  # old -> new direction

    def spiral(width, height):
        if width < 1 or height < 1:
            raise ValueError
        x, y = width // 2, height // 2  # start near the center
        dx, dy = NORTH  # initial direction
        matrix = [[None] * width for _ in range(height)]
        count = 0
        while True:
            count += 1
            matrix[y][x] = count  # visit
            # try to turn right
            new_dx, new_dy = turn_right[dx, dy]
            new_x, new_y = x + new_dx, y + new_dy
            if (0 <= new_x < width and 0 <= new_y < height and
                    matrix[new_y][new_x] is None):  # can turn right
                x, y = new_x, new_y
                dx, dy = new_dx, new_dy
            else:  # try to move straight
                x, y = x + dx, y + dy
                if not (0 <= x < width and 0 <= y < height):
                    return matrix  # nowhere to go

    m = spiral(527, 527)
    xStart = yStart = xEnd = yEnd = -1
    for y, line in enumerate(m):
        for x, e in enumerate(line):
            if e == 1:
                xStart = x
                yStart = y
            elif e == 277678:  # My input
                xEnd = x
                yEnd = y
    return abs(xStart - xEnd) + abs(yStart - yEnd)


def p2():
    NORTH, S, W, E = (0, 1), (0, -1), (-1, 0), (1, 0)  # directions
    turn_right = {NORTH: E, E: S, S: W, W: NORTH}  # old -> new direction

    def spiral(width, height):
        if width < 1 or height < 1:
            raise ValueError
        x, y = width // 2, height // 2  # start near the center
        dx, dy = NORTH  # initial direction
        matrix = [[None] * width for _ in range(height)]
        count = 0
        while True:
            count += 1
            matrix[y][x] = 1 if count == 1 else sum_neighbors(x, y, matrix, width, height)  # visit
            if matrix[y][x] > 277678: #My input
                return matrix[y][x]
            # try to turn right
            new_dx, new_dy = turn_right[dx, dy]
            new_x, new_y = x + new_dx, y + new_dy
            if (0 <= new_x < width and 0 <= new_y < height and
                    matrix[new_y][new_x] is None):  # can turn right
                x, y = new_x, new_y
                dx, dy = new_dx, new_dy
            else:  # try to move straight
                x, y = x + dx, y + dy
                if not (0 <= x < width and 0 <= y < height):
                    return matrix  # nowhere to go

    def sum_neighbors(x, y, matrix, width, height):
        l = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
             (x + 1, y + 1)]
        s = 0
        for e in l:
            if width > e[0] >= 0 and height > e[1] >= 0 and matrix[e[1]][e[0]] is not None:
                s += matrix[e[1]][e[0]]
        return s

    return spiral(527,527)


if __name__ == '__main__':
    print(f'Part 1 : {p1()}')
    print(f'Part 2 : {p2()}')
