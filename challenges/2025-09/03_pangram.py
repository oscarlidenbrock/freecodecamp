# Daily challenge 2025-09-03: Pangram
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-03
#
# Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.
# 
# Ignore non-alphabetical characters in the word or sentence.
# Ignore letter casing in the word or sentence.
# 

from typing import TypedDict


# Challenge
def is_pangram(sentence: str, letters: str) -> bool:
    """
    Check if a sentence contains all and only the specified letters.

    A sentence is considered valid if:
    - Every letter in the sentence is in the provided set of letters.
    - All letters in the provided set appear at least once in the sentence.
    Non-letter characters are ignored.

    :param sentence: The sentence to check
    :param letters: The set of allowed letters
    :return: True if the sentence uses only the given letters and includes all of them, otherwise False
    """

    # Convert both sentence and allowed letters to lowercase
    sentence = sentence.lower()
    letters = letters.lower()
    characters_seen = ""

    # Iterate through each character in the sentence
    for char in sentence:
        # Only consider lowercase alphabetic characters
        if 'a' <= char <= 'z':
            # If the character is not in the allowed letters, return False
            if char not in letters:
                return False

            # Keep track of characters we have seen
            if char not in characters_seen:
                characters_seen += char

    # Check if all allowed characters were used at least once
    return len(characters_seen) == len(letters)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["hello", "helo"], "result": True},
        {"parameters": ["hello", "hel"], "result": False},
        {"parameters": ["hello", "helow"], "result": False},
        {"parameters": ["hello world", "helowrd"], "result": True},
        {"parameters": ["Hello World!", "helowrd"], "result": True},
        {"parameters": ["Hello World!", "heliowrd"], "result": False},
        {"parameters": ["freeCodeCamp", "frcdmp"], "result": False},
        {"parameters": ["The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz"], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_pangram(test['parameters'][0], test['parameters'][1])
        if result == test['result']:
            print("OK\r")

            print(f"INPUT: ", test['parameters'])
            print(f"RETURN: ", result)
            print("======================\r")
        else:
            print("ERROR\r")

            print(f"INPUT: ", test['parameters'])
            print(f"RETURN: ", result)
            print(f"EXPECTED: ", test['result'])
            print("======================\r")

            if len(debug_messages) > 0:
                print("DEBUG:")
                for msg in debug_messages:
                    print(f"", msg[0], ": ", msg[1])

            print("")
            answer = input("Continue with the next test? [y/n] ")
            print("")

            if not (answer == "y" or answer == ""): return

debug_messages = []


def debug(type, message):
    debug_messages.append([type, message])

test()