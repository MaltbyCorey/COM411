import matplotlib.pyplot as plt


def coordinate():
    print("Please enter the x value")
    x = int(input())
    print("Please enter the y value")
    y = int(input())

    coordinates = (x, y)
    return coordinates


def path():
    print("Retrieving path...")

    x_value = []
    y_value = []

    for i in range(4):
        data = coordinate()
        x_value.append(data[0])
        y_value.append(data[1])

    return [x_value, y_value]


def run():
    values = path()
    plt.plot(values[0], values[1], 'ro--')
    plt.show()


run()
