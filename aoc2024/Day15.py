import time


def p1(grid, movements):
    robotX, robotY = 0, 0
    for x, line in enumerate(grid):
        for y, v in enumerate(line):
            if v == "@":
                robotX = x
                robotY = y
                break

    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    for movement in movements:
        direction = directions[movement]
        newX, newY = robotX + direction[0], robotY + direction[1]
        # If it's not a wall
        if 0 < newX < len(grid) and 0 < newY < len(grid[0]) and grid[newX][newY] != "#":
            # If it's a free space
            if grid[newX][newY] == ".":
                # Move the robot and go to the next loop
                grid[newX][newY] = "@"
                grid[robotX][robotY] = "."
                robotX, robotY = newX, newY
                continue
            # If here, it can only be a box. We find how many and if there's a free space, we push them
            while grid[newX][newY] == "O":
                newX += direction[0]
                newY += direction[1]
            if grid[newX][newY] == "#":
                continue
            # It can only be a free space
            grid[newX][newY] = "O"
            grid[robotX][robotY] = "."
            robotX += direction[0]
            robotY += direction[1]
            grid[robotX][robotY] = "@"

    total = 0
    for x, line in enumerate(grid):
        for y, v in enumerate(line):
            if v == "O":
                total += 100 * x + y
    return total


def p2(grid, movements):
    grid = doubleGrid(grid)
    robotX, robotY = 0, 0
    for x, line in enumerate(grid):
        for y, v in enumerate(line):
            if v == "@":
                robotX = x
                robotY = y
                break

    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    for movement in movements:
        direction = directions[movement]
        newX, newY = robotX + direction[0], robotY + direction[1]
        # If it's not a wall
        if 0 < newX < len(grid) and 0 < newY < len(grid[0]) and grid[newX][newY] != "#":
            # If it's a free space, move the robot
            if grid[newX][newY] == ".":
                grid[newX][newY] = "@"
                grid[robotX][robotY] = "."
                robotX, robotY = newX, newY
                continue
            # It can only be a box
            # We change the newY if it's a ] to ALWAYS check from the [ to more easily keep track of the boxes
            if grid[newX][newY] == "]":
                newY -= 1
            if canMove(grid, newX, newY, movement, directions):
                if movement in ("<", ">"):
                    grid[robotX][robotY] = "."
                    robotY += direction[1]
                    grid[robotX][robotY] = "@"
                    newY += direction[1] if movement == ">" else 0
                    while grid[newX][newY] in ("[", "]"):
                        grid[newX][newY] = "[" if grid[newX][newY] == "]" else "]"
                        newY += direction[1]
                    grid[newX][newY] = "]" if movement == ">" else "["
                else:
                    grid = move(grid, newX, newY, direction)
                    grid[robotX][robotY] = "."
                    robotX += direction[0]
                    grid[robotX][robotY] = "@"

    total = 0
    for x, line in enumerate(grid):
        for y, v in enumerate(line):
            if v == "[":
                total += 100 * x + y
    return total


def doubleGrid(grid):
    newGrid = []
    doubles = {"#": ["#", "#"], "O": ["[", "]"], ".": [".", "."], "@": ["@", "."]}
    for line in grid:
        newLine = []
        for x in line:
            newLine += doubles[x]
        newGrid.append(newLine)
    return newGrid


def canMove(grid, x, y, movement, directions):
    if movement == "<":
        newX = x + directions[movement][0]
        newY = y + directions[movement][1]
        if grid[newX][newY] == ".":
            return True
        if grid[newX][newY] == "#":
            return False
        return canMove(grid, newX, newY - 1, movement, directions)

    if movement == ">":
        newX = x + directions[movement][0]
        newY = y + 2 * directions[movement][1]
        if grid[newX][newY] == ".":
            return True
        if grid[newX][newY] == "#":
            return False
        return canMove(grid, newX, newY, movement, directions)

    # Movement is either ^ or v
    newX = x + directions[movement][0]
    newYLeft = y
    newYRight = y + 1
    # Example of this case :
    # ..
    # []
    if grid[newX][newYLeft] == "." and grid[newX][newYRight] == ".":
        return True
    # Example of this case :
    # .#
    # []
    if grid[newX][newYLeft] == "#" or grid[newX][newYRight] == "#":
        return False
    # Example of this case :
    # []
    # []
    if grid[newX][newYLeft] == "[":
        return canMove(grid, newX, newYLeft, movement, directions)
    # Example of this case :
    # .[]
    # []
    if grid[newX][newYRight] == "[" and grid[newX][newYLeft] == ".":
        return canMove(grid, newX, newYRight, movement, directions)
    # Example of this case :
    # [].
    #  []
    if grid[newX][newYLeft] == "]" and grid[newX][newYRight] == ".":
        return canMove(grid, newX, newYLeft - 1, movement, directions)
    # There are two boxes either under or above
    # Example of this case :
    # [][]
    #  []
    return canMove(grid, newX, newYLeft - 1, movement, directions) and canMove(
        grid, newX, newYRight, movement, directions
    )


def move(grid, x, y, direction):
    # Move is ONLY for up and down directions
    if grid[x + direction[0]][y] == "[":
        grid = move(grid, x + direction[0], y, direction)
    if grid[x + direction[0]][y] == "]":
        grid = move(grid, x + direction[0], y - 1, direction)
    if grid[x + direction[0]][y + 1] == "[":
        grid = move(grid, x + direction[0], y + 1, direction)
    grid[x][y] = "."
    grid[x][y + 1] = "."
    grid[x + direction[0]][y] = "["
    grid[x + direction[0]][y + 1] = "]"
    return grid


if __name__ == "__main__":
    # I use the same grids twice else p1() changes the grid and fucks my p2()
    grid1, grid2, movements = [], [], []
    with open("input.txt", "r") as f:
        addToGrid = True
        for line in f.readlines():
            line = line.strip()
            if line == "":
                addToGrid = False
            else:
                if addToGrid:
                    grid1.append(list(line))
                    grid2.append(list(line))
                else:
                    movements += list(line)
    start = time.time()
    print(f"Part 1 : {p1(grid1, movements)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 3.64 ms
    start = time.time()
    print(f"Part 2 : {p2(grid2, movements)}")
    print(f"Time for part 2 : {time.time() - start}s")  # 4.99 ms
