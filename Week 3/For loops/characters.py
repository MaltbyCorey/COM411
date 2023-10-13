print("What word do you see?")
word = input()
for position in range(0, len(word), 1):
    print(f"Index {position}: {word[position]}")
print("Done!")