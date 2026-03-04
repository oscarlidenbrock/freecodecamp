# Daily challenge 2026-02-28: Add Punctuation
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-28
#
# Given a string of sentences with missing periods, add a period (".") in the following places:
# 
# Before each space that comes immediately before an uppercase letter
# And at the end of the string
# 
# Return the resulting string.

from typing import TypedDict


# Challenge
def add_punctuation(sentence: str) -> str:
    """
    Return the sentences with end sentence dots.
    :param sentence: Sentences in one string.
    :return: Sentences with dots.
    """

    result = ""
    last_character = ""

    for word in sentence:
        if ord(word) >= ord("A") and ord(word) <= ord("Z") and last_character == " ":
            # add end line dot
            result = result[:-1] + ". " + word
        else:
            result += word

        last_character = word

    # Add final dot
    result += "."

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["Hello world"], "result": "Hello world."},
        {"parameters": ["Hello world It's nice today"], "result": "Hello world. It's nice today."},
        {"parameters": ["JavaScript is great Sometimes"], "result": "JavaScript is great. Sometimes."},
        {"parameters": ["A b c D e F g h I J k L m n o P Q r S t U v w X Y Z"], "result": "A b c. D e. F g h. I. J k. L m n o. P. Q r. S t. U v w. X. Y. Z."},
        {"parameters": ["Wait.. For it"], "result": "Wait... For it."},
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if add_punctuation(test['parameters'][0]) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")

test()