# Asks the user what book type they have
print("What type of cover does the book have?")
book_cover = input("")

# Branchs depending on input
if book_cover == "soft":
    # Asks the user if the book is perfect-bound
    print("Is the book perfect-bound?")
    answer = input("").lower()

    # Branchs based on input
    if answer == "yes":
        # Book is perfect bound
        print("Soft cover, perfect bound books are very popular!")
    else:
        # Book is not perfect bound
        print("Soft covers with coils or stitches are great for short books")
elif book_cover == "hard":
    print("Books with hard covers can be more expensive!")



