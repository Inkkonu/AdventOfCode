import matplotlib.pyplot as plt
import matplotlib.animation as animation


def p1(data):
    return sum([1 if c == '(' else -1 for c in data[0]])


def p1Visualisation(data, saveToVideo=False):
    floor = i = 0

    x = [i]
    y = [floor]
    yMargin = 50

    fig, ax = plt.subplots()
    graph = ax.plot(x, y, color='g')[0]
    plt.title("AoC - Part 1 of Day 1 of 2015")
    plt.xlabel("Step")
    plt.ylabel("Floor")

    def update(frame):
        nonlocal floor, i  # To avoid an UnboundLocalError
        if i >= len(data[0]):
            return
        floor += 1 if data[0][i] == "(" else -1
        x.append(i+1)
        y.append(floor)
        i += 1

        graph.set_xdata(x)
        graph.set_ydata(y)
        plt.xlim(x[0], x[-1])
        plt.ylim(min(y)-yMargin, max(y)+yMargin)

    anim = animation.FuncAnimation(fig, update, frames=None,
                                   interval=1, cache_frame_data=False)

    if saveToVideo:
        anim.save("Videos/AoC-2015-01-P1.mp4",
                  writer=animation.FFMpegWriter(fps=60))
        plt.close()
    else:
        plt.show()


def p2(data):
    floor = 0
    for i, c in enumerate(data[0]):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return i+1


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
    # No visualisation for part 2 as it would be the same as part 1 but cutting earlier
    p1Visualisation(data, True)
