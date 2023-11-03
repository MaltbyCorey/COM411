import csv


def read_csv(filename):
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)

        headings = next(csv_reader)
        print(f'Headings:\n{headings}')

        print('Values:')
        for line in csv_reader:
            print(line)


def run():
    read_csv('clothing.csv')


if __name__ == "__main__":
  run()
