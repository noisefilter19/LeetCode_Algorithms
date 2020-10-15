import sys
import time
import random
from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib.animation as animation


values = []
elapsed = 0

def gen_values(range_):
    for x in range(range_):
        x += 1
        values.append(x)
    random.seed(time.time())
    random.shuffle(values)


def quicksort_algorithim(values, start, end):
    def swap(values, i, j):
        if i != j:
            values[i], values[j] = values[j], values[i]

    if start >= end:
        return

    pivot = values[end]
    pivot_index = start

    for x in range(start, end):
        if values[x] < pivot:
            swap(values, x, pivot_index)
            pivot_index += 1
        yield values

    swap(values, end, pivot_index)
    yield values

    yield from quicksort_algorithim(values, start, pivot_index - 1)
    yield from quicksort_algorithim(values, pivot_index + 1, end)

def update(values, bar, iteration, text):
    for rect, value in zip(bar, values):
        rect.set_height(value)

    iteration[0] += 1


    elapsed = (time.time() - start)
    text.set_text("[+] Runtime: {}".format(str(timedelta(seconds=elapsed))))


def animate(values, range_):
    fig, ax = plt.subplots()
    fig.canvas.set_window_title('Quick Sorting Algorithm')
    ax.set_title('Quick Sorting Algorithm')

    bar = ax.bar(range(len(values)), values, align = 'edge')

    ax.set_xlim(0, range_)
    ax.set_ylim(0, int(1.07 * range_))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    update(values, bar, iteration, text)
    animation_ = animation.FuncAnimation(fig, func = update,
            fargs=(bar, iteration, text), frames=quicksort_algorithim(values, 0, range_ - 1), interval=1,
            repeat=False)
    plt.show()



if __name__ == '__main__':
    try:
        range_ = int(input('[+] Enter the number of values to generate: '))
    except:
        print('\n[!] Error: Exiting.')
        sys.exit()

    gen_values(range_)

    quicksort_algorithim(values, 0, range_ - 1)
    start = time.time()
    animate(values, range_)
