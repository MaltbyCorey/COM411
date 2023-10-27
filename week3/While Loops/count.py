# Gets the amount of obstacles
print("How many obstacles must I avoid?")
obstacles = int(input())

# Loops until count is equal to obstacles
for count in range(obstacles):
    print(f"Avoiding...Done! {count + 1} obstacles avoided.")
    count += 1
    # Increments count and loops back
print("All obstacles have been avoided")
