from week10.inhabitant import Inhabitant


class Robot(Inhabitant):
    # Instant Method
    def display(self):
        print(f"I am {self.name}")

    # Magic Method
    def __repr__(self):
        return f"Robot(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"My name is {self.name}, I am {self.age} years old and my energy is {self.energy}"
