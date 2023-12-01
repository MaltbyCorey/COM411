from week10.planet import Planet
from week10.human import Human
from week10.robot import Robot
import random as random
import matplotlib.pyplot as plt


class Universe:
    # Initializer
    def __init__(self):
        self.planets = []

    def __repr__(self):
        return f"universe(planet={self.planets})"

    def __str__(self):
        return f"The universe contains {len(self.planets)} planets"

    def generate(self):
        planet = Planet()

        # Population
        for index in range(random.randint(1, 10)):
            human = Human(f"Human{index}")
            planet.add(human)

        for index in range(random.randint(1, 10)):
            robot = Robot(f"Robot{index}")
            planet.add(robot)

        self.planets.append(planet)

    def show_population(self, selection):

        num_subplot = len(self.planets)

        fig = plt.figure()

        for index in range(num_subplot):
            planet = self.planets[index]

            num_humans = 0
            num_robots = 0

            for inhabitant in planet.inhabitant:
                if isinstance(inhabitant, Human):
                    num_humans += 1
                elif isinstance(inhabitant, Robot):
                    num_robots += 1

            ax = fig.add_subplot(1, num_subplot, index + 1)
            ax.bar([1, 2], [num_humans, num_robots])

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    universe = Universe()
    universe.generate()
    universe.show_population("humans")
    universe.show_population("robots")
