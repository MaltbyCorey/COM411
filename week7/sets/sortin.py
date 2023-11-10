def observed_items():
    observations = []

    for count in range(5):
        print("Please enter a observation")
        observations.append(input())

    return observations


def remove_observations(observations):
    running = True

    while running:
        print("Do you wish to remove an observation (yes/no)?")
        response = input()

        if response == "yes":
            print("Enter the observation to remove")
            observation = input()
            observations.remove(observation)
        else:
            running = False


def run():
    observations = observed_items()
    remove_observations(observations)

    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    for data in sorted(observations_set):
        print(f"{data[0]} observed {data[1]} times")


run()
