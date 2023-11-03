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


def run():
    local_data('titanic.csv')
    num_records = len(records)
    print(f"Successfully loaded {num_records} records")


if __name__ == "__main__":
  run()