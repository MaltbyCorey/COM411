# Climbing ladder function
def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        return "Still some way to go!"
    else:
        return "We are almost there!"


print(climb_ladder(5, 2))
print(climb_ladder(2, 5))
