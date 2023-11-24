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


