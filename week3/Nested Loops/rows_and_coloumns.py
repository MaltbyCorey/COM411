# Gets rows and coloumns from user
print("How many rows should I have?")
rows = int(input())
print("How many columns should I have?")
columns = int(input())

# Loops for rows
for row in range(0, rows, 1):
    # Loops for columns
    for column in range(0, columns, 1):
        print(":-)", end="")
    print("")
