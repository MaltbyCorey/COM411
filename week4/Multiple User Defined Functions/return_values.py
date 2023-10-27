# Gets the total weight
def sum_weights(character_weight, inventory_weight):
    total_weight = character_weight + inventory_weight
    return total_weight


# Calculates the average weight
def calc_avg_weight(character_weight,inventory_weight):
    average_weight = sum_weights(character_weight, inventory_weight) / 2
    return average_weight


# Function to run
def run():
    print("Enter the characters weight")
    character_weight = int(input())
    print("Enter the inventory weight")
    inventory_weight = int(input())

    print("sum or average?")
    feature = input()

    if feature == "sum":
        return sum_weights(character_weight, inventory_weight)
    else:
        return calc_avg_weight(character_weight, inventory_weight)


print(run())
