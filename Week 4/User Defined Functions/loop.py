# Crossing bridge function
def cross_bridge(steps):
    # Display each step
    for step in range(steps):
        print("Crossed step.")

    # Displaying message
    if steps > 5:
        return "The bridge is collapsing!"
    else:
        return "we must keep going!"


print(cross_bridge(3))
print(cross_bridge(6))

