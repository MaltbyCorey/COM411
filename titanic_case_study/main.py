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
        [5] Display the number of survivors per age group
        """)

    # Returns the users input
    return int(input())


# Option 1
# Displays all the passengers names
def display_passenger_names():
    print("The names of the passengers are: \n")

    # Loops until all records have been used
    for record in records:
        passenger_name = record[3]
        if passenger_name != "":
            print(passenger_name)


# Option 2
# Displays the total number of survivors
def display_number_survivors():
    num_survived = 0

    # Loops until all records have been used
    for record in records:
        # If the survived column contains 1 add it to the total survived
        status = int(record[1])
        if status == 1:
            num_survived += 1

    print(f"{num_survived} passengers survived")


# Option 3
# Displays the number of passengers per gender
def display_passenger_per_gender():
    females = 0
    males = 0

    # Loops until all records have been used
    for record in records:
        gender = record[4]
        # Adds to the total depending on gender
        if gender == "female":
            females += 1
        elif gender == "male":
            males += 1

    print(f"females: {females}, males: {males}")


# Option 4
# Displays the number of passengers per age group
def display_passenger_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    # Loops until all records have been used
    for record in records:
        # Checks to see if there is a value for age
        if record[5] != "":
            age = float(record[5])
            # Adds to the total for the corresponding age group
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")


# Option 5
# Displays the total number of survives in each age group
def display_survivors_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    children_survived = 0
    adults_survived = 0
    elderly_survived = 0

    # Loops until all records have been used
    for record in records:
        # Checks to see if there is a value for age
        if record[5] != "":
            age = float(record[5])
            survived = int(record[1])

            # Gets the total per age group and the total survived per age group
            if age < 18:
                children += 1
                if survived == 1:
                    children_survived += 1
            elif age < 65:
                adults += 1
                if survived == 1:
                    adults_survived += 1
            else:
                elderly += 1
                if survived == 1:
                    elderly_survived += 1

    print(f"children: {children_survived}/{children}, adults: {adults_survived}/{adults}, elderly: {elderly_survived}/{elderly}")


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

    # Runs the function corresponding to the option selected
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_number_survivors()
    elif selected_option == 3:
        display_passenger_per_gender()
    elif selected_option == 4:
        display_passenger_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised")


if __name__ == "__main__":
    run()
