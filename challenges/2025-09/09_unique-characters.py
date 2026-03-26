# Daily challenge 2025-09-09: Unique Characters
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-09
#
# Given a string, determine if all the characters in the string are unique.
# 
# Uppercase and lowercase letters should be considered different characters.
# 

from typing import TypedDict


# Challenge
def all_unique(input: str) -> bool:
    """
    Check whether the string contains only unique characters.

    :param input: The string to evaluate
    :return: True if all characters are unique, otherwise False
    """

    # Iterate through each character in the string
    for char in input:
        # If the character appears more than once, it's not unique
        if input.count(char) > 1:
            return False

    # If no duplicates were found, all characters are unique
    return True

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["abc"], "result": True},
        {"parameters": ["aA"], "result": True},
        {"parameters": ["QwErTy123!@"], "result": True},
        {"parameters": ["~!@#$%^&*()_+"], "result": True},
        {"parameters": ["hello"], "result": False},
        {"parameters": ["freeCodeCamp"], "result": False},
        {"parameters": ["!@#*$%^&*()aA"], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = all_unique(test['parameters'][0])
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