"""This is a program like wordle."""

__author__ = "730439833"

word: str = str(input("Enter a 5 character word: "))
if len(word) != 5:
    print("Error: word must contain 5 characters")
    exit()

char: str = str(input("Enter a single character: "))
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

print(str(count) + " instances of " + char + " found in " + word)