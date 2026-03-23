# Daily challenge 2026-03-23: No Consecutive Repeats
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-23
#
# Given a string, determine if it has no repeating characters.
# 
# A string has no repeats if it does not have the same character two or more times in a row.
# 

from typing import TypedDict
import re

# Challenge
def has_no_repeats(input: str) -> bool:
    """
    Check whether a string contains no consecutive repeated characters.

    A string is considered valid if no character appears twice in a row.

    :param input: The string to evaluate
    :return: False if any character is repeated consecutively, otherwise True
    """

    # Search for any character immediately followed by the same character
    match = re.search(r'(.)\1', input)

    if match:
        # Log the first duplicated consecutive character found
        debug("duplicated character", match.group(1))
        return False

    return True

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["hi world"], "result": True},
        {"parameters": ["hello world"], "result": False},
        {"parameters": ["abcdefghijklmnopqrstuvwxyz"], "result": True},
        {"parameters": ["freeCodeCamp"], "result": False},
        {"parameters": ["The quick brown fox jumped over the lazy dog."], "result": True},
        {"parameters": ["Mississippi"], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = has_no_repeats(test['parameters'][0])
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