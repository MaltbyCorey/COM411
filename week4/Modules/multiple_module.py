# Importing modules
import week1.input_tasks as wk1_input
import week1.output_tasks as wk1_output


def run_week_one():
    print("Which program in Week 1 do you wish to run?")
    response = input()
    if response == "input":
        wk1_input.lives_task()
    elif response == "output":
        wk1_output.main()


def run():
    while True:
        print("What would you like to do?")
        print("[a] Run 'week 1' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_week_one()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")


run()
