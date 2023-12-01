from week10.human import Human
from week10.robot import Robot


class Planet:
    # Initializer
    def __init__(self):
        self.inhabitant = []

    def __repr__(self):
        return f"Planet(Inhabitants={self.inhabitant}"

    def __str__(self):
        return f"The planet has {len(self.inhabitant)}"

    # Instance Methods
    def add(self, inhabitant):
        self.inhabitant.append(inhabitant)

    def remove(self, inhabitant):
        self.inhabitant.remove(inhabitant)


if __name__ == "__main__":
    planet = Planet()
    print(repr(planet))
    prins = Human("Prins")
    planet.add(prins)
    print(repr(planet))
    print(planet)
