class Human:
    # Class Constant Attribute
    MAX_ENERGY = 100

    # Initializer
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.energy = Human.MAX_ENERGY

    # Instance Method
    def display(self):
        print(f"I am {self.name}")

    # Magic Method
    def __repr__(self):
        return f"Human(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"My name is {self.name}, I am {self.age} years old and my energy is {self.energy}"

    # Instant Method
    def grow(self):
        self.age += 1

    def eat(self, amount):
        new_energy = amount + self.energy
        if new_energy > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY
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


if __name__ == "__main__":
    human = Human("Human")
    print(repr(human))
    human.move(10)
    print(repr(human))
    human.eat(5)
    print(repr(human))
    human.eat(20)
    print(repr(human))
