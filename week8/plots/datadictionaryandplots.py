import matplotlib.pyplot as plt
import random


def data():
    paths = {}

    print("What type of line (:, -- or -)?")
    line_type = input()

    print("What colour (r, g or b)?")
    colour = input()

    print("What type of marker (o, s or ^)?")
    marker_style = input()

    paths['line_style'] = line_type
    paths['colour'] = colour
    paths['marker_style'] = marker_style

    return paths


def generate():
    print("How many of lines do you want to display?")
    line_num = int(input())

    for i in range(line_num):
        values = data()
        format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
        x = random.sample(range(1, 10), 5)
        y = random.sample(range(1, 10), 5)
        plt.plot(x, y, format)

    plt.show()


def run():
    print("Running...")
    generate()
    print("Done.")


run()
