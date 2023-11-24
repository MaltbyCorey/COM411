from week9.planet import Planet
from week9.human import Human
from week9.robot import Robot
import random as random
import matplotlib.pyplot as plt


class Universe:
    # Initializer
    def __init__(self):
        self.planets = []

    # Instance Method
    def generate(self):
        for num in range(random.randint(1, 10)):
            # Name
            planet = Planet(f"Planet {num}")

        # Population
            for index in range(random.randint(1, 10)):
                human = Human(f"Human{index}")
                planet.add_human(human)

            for index in range(random.randint(1, 10)):
                robot = Robot(f"Robot{index}")
                planet.add_robot(robot)

            self.planets.append(planet)

    def show_population(self, selection):
        x_values = []
        y_values = []

        for planet in self.planets:
            x_values.append(planet.name)
            if selection == "human":
                y_values.append(len(planet.citizens['humans']))
            else:
                y_values.append(len(planet.citizens['robots']))#

            plt.bar(x_values, y_values)
            plt.tight_layout()
            plt.show()
