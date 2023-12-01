from week10.inhabitant import Inhabitant


class Alien(Inhabitant):

    def __init__(self):
        super().__init__()
        self.technology = []

    def __str__(self):
        return f"Alien has: {self.technology}"

    def __repr__(self):
        return f"Alien(technology={self.technology}"

    def pickup(self, technology):
        self.technology.append(technology)

    def drop(self, technology):
        self.technology.remove(technology)


if __name__ == "__main__":
    alien = Alien()
    print(repr(alien))
