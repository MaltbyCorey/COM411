class Human:
    # Class Constant Attribute
    MAX_ENERGY = 100

    # Initializer
    def __init__(self):
        self.name = "Human"
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

