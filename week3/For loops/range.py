print("What level of brightness is required?")
brightness_required = int(input())

print("Adjusting brightness...")

for brightness in range(2, brightness_required + 1, 2):
    print(f"Brightness level: {'*' * brightness}")

print("Complete!")