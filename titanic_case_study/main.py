import csv

records = []
headings = []


# Gets the heading and data from the csv file
def local_data(file_path):
    print("Loading data...", end="")
    # Opens the titanic dataset
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        # Adds the heading into the global variable
        headings.append(next(csv_reader))

        # Adds each line into the records list
        for line in csv_reader:
            records.append(line)

    print("Done.")


# Displays the menu to the user
def display_menu():
    print(
        """
        Please select one of the following options:
        [1] Display the names of all passengers
        [2] Display the number of passengers that survived
        [3] Display the number of passengers per gender
        [4] Display the number of passengers per age group
        [5] Display the number of survivors per age group"
        """)

    # Returns the users input
    return int(input())


# Runs the program
def run():
    # Loads the dataset
    local_data('titanic.csv')
    # Gets the total amount of records loaded
    num_records = len(records)
    # Displays the total records to the user
    print(f"Successfully loaded {num_records} records")

    # Displays the menu and gets the option chose
    selected_option = display_menu()
    print(f"You have selected option {selected_option}")


if __name__ == "__main__":
    run()
