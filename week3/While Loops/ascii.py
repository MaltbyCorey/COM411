print("How many bars should be charged?")
bars_to_charge = int(input())
bars_charged = 0


while bars_charged < bars_to_charge:
    # Incrementing bars_charged
    bars_charged += 1
    print(f"Charging: {'█' * bars_charged}")


