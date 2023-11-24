from week9.human import Human
from week9.robot import Robot


class Planet:
    # Initializer
    def __init__(self, name):
        self.name = name
        self.citizens = {
            "humans": [],
            "robots": []
        }

    # Instance Methods
    def add_human(self, human):
        self.citizens["humans"].append(human)

    def remove_human(self, human):
        self.citizens["humans"].remove(human)

    def add_robot(self, robot):
        self.citizens["robots"].append(robot)

    def remove_robot(self, robot):
        self.citizens["robots"].remove(robot)

    # Magic Method
    def __repr__(self):
        return f"Planet(human={self.citizens['humans']}, Robots(robot={self.citizens['robots']}"

    def __str__(self):
        return f"The planet has {len(self.citizens['humans'])} humans and {len(self.citizens['robots'])}"


if __name__ == "__main__":
    planet = Planet("Earth")
    print(repr(planet))
    prins = Human("Prins")
    planet.add_human(prins)
    print(repr(planet))
    print(planet)

