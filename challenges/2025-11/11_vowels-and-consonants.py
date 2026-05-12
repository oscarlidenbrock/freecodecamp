# Daily challenge 2025-11-11: Vowels and Consonants
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-11
#
# Given a string, return an array with the number of vowels and number of consonants in the string.
# 
# Vowels consist of a, e, i, o, u in any case.
# Consonants consist of all other letters in any case.
# Ignore any non-letter characters.
# 
# For example, given "Hello World", return [3, 7].

from typing import TypedDict


# Challenge
def count(text: str) -> list[int]:
    """
    Return the number of vowels and number of consonants in the string.

    :param text: The string to analyze.
    :return: Returns a list with the number of vowels and number of consonants.
    """

    result = [0, 0]

    for char in text.lower():
        if char in "aeiou":
            result[0] += 1
        elif char.isalpha():
            result[1] += 1

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": ["Hello World"], "result": [3, 7]},
        {"parameters": ["JavaScript"], "result": [3, 7]},
        {"parameters": ["Python"], "result": [1, 5]},
        {"parameters": ["freeCodeCamp"], "result": [5, 7]},
        {"parameters": ["Hello World"], "result": [3, 7]},
        {"parameters": ["Hello World"], "result": [3, 7]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = count(test['parameters'][0])
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