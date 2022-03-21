"""Wordle like the real game."""

__author__ = "730403391"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret_word: str, guess_char: str) -> bool:
    """When given two strings will return True if char found at any index of the first string, and return False otherwise."""
    i: int = 0
    result: bool = False
    assert len(guess_char) == 1
    while i < len(secret_word):
        if secret_word[i] == guess_char:
            result = True
            return result
        else:
            i += 1
    if result is not True:
        return result


def emojified(guess_word: str, secret_word: str) -> str:
    """Generates the emoji string."""
    result: str = ""
    if len(guess_word) != len(secret_word):
        raise AssertionError
    i: int = 0
    while i < len(guess_word):
        if contains_char(secret_word, guess_word[i]):
            if secret_word[i] == guess_word[i]:
                result += GREEN_BOX
                i += 1
            else:
                result += YELLOW_BOX
                i += 1
        else:
            result += WHITE_BOX
            i += 1
    return result


def input_guess(expected_length: int) -> str:
    """Checks to see if lengths equal each other."""
    guess: str = input(f"Enter a {expected_length} letter word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} characters! Try again: ")
    return guess


def main() -> None:
    """Entry point."""
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    has_won: bool = False
    while (turns < 7) & (has_won is not True):
        print(f"=== Turn {turns}/6 ===")
        guess_word: str = input_guess(len(secret_word))
        print(emojified(guess_word, secret_word))
        if secret_word == guess_word:
            has_won = True
            print(f"You won in {turns}/6 turns!")
        else:
            turns += 1
    if (has_won is not True):
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()