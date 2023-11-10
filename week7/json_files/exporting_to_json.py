import  json


def read(filename):
    print("Reading...")

    with open(filename) as file:
        data = json.load(file)

    print("Done.")
    return data


def save(filename, save_data):
    print("Exporting...")
    with open(filename, 'w') as file:
        json.dump(save_data, file, indent=4)

    print("Done.")


def run():
    json_data = read("futurama.json")
    save("futurama.json", json_data)


run()