def functions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def run_task1():
    print(functions())


# Ensures the function can only be called if it is executed directly and not imported
if __name__ == "__main__":
    run_task1()
