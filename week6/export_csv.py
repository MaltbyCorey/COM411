import csv


def export_csv(filename, item_num):
    print('Exporting...')

    with open(filename, 'a') as csvfile:
        for count in range(item_num):
            print('enter the id of the item')
            item_id = input()
            print('enter the name of the item')
            item_name = input()
            print('enter the colour of the item')
            item_colour = input()

        data = f'{item_id}, {item_name}, {item_colour}\n'

        csvfile.write(data)

    print('Done.')


def run():
    export_csv('exported_items.csv', 2)


if __name__ == "__main__":
    run()
