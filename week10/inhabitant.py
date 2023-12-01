from abc import ABC


class Inhabitant(ABC):
    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = Inhabitant.MAX_ENERGY

    def __str__(self):
        return f"My name is {self.name}, I am {self.age} years old and my energy is {self.energy}"

    # Instant Method
    def grow(self):
        self.age += 1

    def eat(self, amount):
        new_energy = amount + self.energy
        if new_energy > Inhabitant.MAX_ENERGY:
            self.energy = Inhabitant.MAX_ENERGY
            return new_energy - self.energy
        else:
            self.energy = new_energy
            return 0

    def move(self, distance):
        new_energy = self.energy - distance
        if new_energy > 0:
            self.energy = new_energy
            return 0
        else:
            self.energy = 0
            return self.energy - abs(new_energy)
