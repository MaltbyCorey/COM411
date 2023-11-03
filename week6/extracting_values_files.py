import csv


def extract(filename):
    print("Extracting...")
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        names = ''
        for value in csv_reader:
            names += f'{value[1]}\n'

    print('Done.')
    print(f'The extracted items are: \n{names}')


def run():
    extract("clothing.csv")


if __name__ == "__main__":
    run()