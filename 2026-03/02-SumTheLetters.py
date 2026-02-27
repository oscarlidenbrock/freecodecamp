# Daily challenge 02/03/2026: Sum the letters
#
# Given a string, return the sum of its letters.
#
# Letters are A-Z in uppercase or lowercase
# Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
# Uppercase and lowercase letters have the same value.
# Ignore all non-letter characters.

from typing import TypedDict


# Challenge
def sum_letters(phrase: str) -> int:
    # Convert the input to uppercase
    phrase = phrase.upper()
    result = 0

    # For each letter in the input…
    for word in phrase:
        # Rest 64 to the ASCII Value (A = 65, B = 66...)
        asc = ord(word) - 64

        # If ASCII Value it's a letter (A-Z), then sum to result
        if asc >= 1 and asc <= 26:
            result += asc

    return result


# Test
def test():
    class UnitTest(TypedDict):
        value: str
        result: int

    unitTest: list[UnitTest] = [
        {"value": "Hello", "result": 52},
        {"value": "freeCodeCamp", "result": 94},
        {"value": "The quick brown fox jumps over the lazy dog.", "result": 473},
        {
            "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.",
            "result": 1681},
        {"value": "</404>", "result": 0}
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if sum_letters(test['value']) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")


test()
