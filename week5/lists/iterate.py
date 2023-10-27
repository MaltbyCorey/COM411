import week5.lists.indexing as indexing


def menu():
    print("Please select a direction")
    movements = indexing.movements()

    # Prints out all the directions
    num = 0
    for direct in [0, 2, 4, 6]:
        print(f"{num}: {movements[direct]}")
        num += 1


def run_task3():
    menu()


if __name__ == "__main__":
    run_task3()