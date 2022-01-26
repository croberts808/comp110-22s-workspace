"""Pseudo wordle with only one guess."""

__author__ = "730439833"

from re import S
import re
from unittest import result


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
resulting_emoji: str = ""

secret_word: str = "python"
prompt: str = input(f"What is your " + str(len(secret_word)) + "-letter guess? ")

while len(prompt) != len(secret_word):
    prompt = input(f"That was not " + str(len(secret_word)) + " letters! Try again:")

i: int = 0

while i < len(secret_word):
    if prompt[i] == secret_word[i]:
        resulting_emoji = resulting_emoji + GREEN_BOX
    else:
        exists: bool = False
        j: int = 0
        while exists != True and j < len(secret_word):
            if secret_word[j] == prompt[i]:
                exists = True
            j += 1
        if exists:
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else:
            resulting_emoji = resulting_emoji + WHITE_BOX
    i += 1

print(resulting_emoji)