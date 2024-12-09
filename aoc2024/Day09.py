def p1(data):
    # Basic two pointers approach
    disk = createDisk(data)
    freeSpaceIndex = disk.index(".")
    fileIndex = len(disk)-1
    while abs(freeSpaceIndex - fileIndex) > 1:
        disk[fileIndex], disk[freeSpaceIndex] = disk[freeSpaceIndex], disk[fileIndex]
        fileIndex -= 1
        while disk[fileIndex] == ".":
            fileIndex -= 1

        freeSpaceIndex += 1
        while disk[freeSpaceIndex] != ".":
            freeSpaceIndex += 1
    return checksum(disk)


def createDisk(data):
    files = data[::2]
    freeSpace = data[1::2] + [0]  # Because freeSpace is shorter than files
    disk = []
    id = 0
    for pair in zip(files, freeSpace):
        for _ in range(pair[0]):
            disk.append(id)
        for _ in range(pair[1]):
            disk.append(".")
        id += 1
    return disk


def checksum(disk):
    total = 0
    for i, v in enumerate(disk):
        total += v*i if v != "." else 0
    return total


def p2(data):
    files = [(i, v) for i, v in enumerate(data[::2])]
    freeSpace = [(".", v) for v in data[1::2]]
    disk = []
    for i in range(len(freeSpace)):
        disk.append(files[i])
        disk.append(freeSpace[i])
    disk.append(files[-1])
    # Disk looks like : [(0,2), (".", 3), (1, 3), (".", 3)...]

    for elem in files[::-1]:
        # For each file, starting from the last
        size = elem[1]
        for i, t in enumerate(disk):
            # Find free space that's big enough
            if t[0] == "." and t[1] >= size:
                disk[i] = (t[0], t[1]-size)
                disk.insert(i, elem)
                # Then replace the file with free space
                for j in range(len(disk)-1, 0, -1):
                    if elem == disk[j]:
                        disk[j] = (".", size)
                        break
                break

    newDisk = []
    for elem in disk:
        for _ in range(elem[1]):
            newDisk.append(elem[0])
    return checksum(newDisk)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
        data = list(map(int, data[0]))
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
