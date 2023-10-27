def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    print("Moving...")
    path = movements()

    # Prints out all items in the list
    x = 1
    for i in [0, 2, 4, 6]:
        print(f"{path[i]} for {path[x]} steps")
        x += 2


if __name__ == "__main__":
    run_task2()
