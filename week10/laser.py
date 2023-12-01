from week10.technology import Technology


class laser(Technology):
    MAX_RANGE = 100

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "laser"

    def activate(self):
        print("laser activated")

    def deactivate(self):
        print("laser deactivated")

    def fire(self, range_dist):
        if range_dist > self.MAX_RANGE:
            print(f"laser fires {laser.MAX_RANGE}")
        else:
            print(f"laser fires {range_dist}")


if __name__ == "__main__":
    laser = laser()
    print(repr(laser))
