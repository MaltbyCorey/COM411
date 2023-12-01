from week10.technology import Technology


class jetpack(Technology):
    MAX_SPEED = 100

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "jetpack"

    def activate(self):
        print("jetpack activated")

    def deactivate(self):
        print("jetpack deactivated")

    def fly(self, speed):
        if speed > self.MAX_SPEED:
            print(f"flying at speed {jetpack.MAX_SPEED}")
        else:
            print(f"flying at speed {speed}")


if __name__ == "__main__":
    jetpack = jetpack()
    print(repr(jetpack))
