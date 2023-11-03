def search_book(filename):
    print('Searching...')
    sections = ''
    books = 'Books:\n'
    with open(filename, 'r') as file:
        for line in file:
            if line.split(None, 1)[0] == 'Section':
                sections += line
            else:
                books += line
    print('Done.')

    return f'{sections}\n\n{books}'


def save(filename, data):
    print('Saving...')
    with open(filename, 'w') as file:
        file.write(data)
    print('Done.')


def run():
    data = search_book('books.txt')
    save('sections-books.txt', data)


if __name__ == "__main__":
    run()
