"""This is a program like wordle."""

__author__ = "730439833"

word: str = str(input("Enter a 5 character word: "))
if len(word) != 5:
    print("Error: word must contain 5 characters")
    exit()

char: str = str(input("Enter a single character: "))
if len(char) != 1:
    print("Error: character must be a single character")
    exit()
count: int = 0

print("Searching for " + char + " in " + word)

if word[0] == char:
    print(char + " found at index 0")
    count += 1
if word[1] == char:
    print(char + " found at index 1")
    count += 1
if word[2] == char:
    print(char + " found at index 2")
    count += 1
if word[3] == char:
    print(char + " found at index 3")
    count += 1
if word[4] == char:
    print(char + " found at index 4")
    count += 1

if count == 1:
    print("1 instance of " + char + " found in " + word)
elif count == 0:
    print("No instances of " + char + " found in " + word)
else:
    print(str(count) + " instances of " + char + " found in " + word)