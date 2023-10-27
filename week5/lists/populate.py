import week5.lists.indexing as indexing


def menu_and_input():
    print("Please select a direction")
    movements = indexing.movements()

    # Prints out all the directions
    num = 0
    for direct in [0, 2, 4, 6]:
        print(f"{num}: {movements[direct]}")
        num += 1
    direction = int(input())

    if direction == 0:
        return "Moving forward"
    elif direction == 1:
        return "Moving backward"
    elif direction == 2:
        return "Turning left"
    elif direction == 3:
        return "Turning right"


def run_task4():
    route = []
    print("Working out escape route...")

    for count in range(5):
        route.append(menu_and_input())

    print(f"Escape route: {route}")


if __name__ == "__main__":
    run_task4()
