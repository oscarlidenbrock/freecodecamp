# Daily challenge 2025-09-23: String Mirror
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-23
#
# Given two strings, determine if the second string is a mirror of the first.
# 
# A string is considered a mirror if it contains the same letters in reverse order.
# Treat uppercase and lowercase letters as distinct.
# Ignore all non-alphabetical characters.
# 

from typing import TypedDict
import re

# Challenge
def is_mirror(str1: str, str2: str) -> bool:
    """
    Determine whether two strings are mirrors of each other.

    The function normalizes both strings by removing all non-alphanumeric
    characters, then checks whether the first string is equal to the
    reversed version of the second string.

    :param str1: First input string.
    :param str2: Second input string.
    :return: True if str1 matches the reverse of str2 after normalization;
             otherwise, False.
    """

    # Normalize both strings by removing non-alphanumeric characters
    str1_clean = re.sub(r'[^a-zA-Z0-9]', '', str1)
    str2_clean = re.sub(r'[^a-zA-Z0-9]', '', str2)

    # Reverse the normalized second string
    str2_clean = str2_clean[::-1]

    # Compare normalized first string with reversed second string
    return str1_clean == str2_clean

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["helloworld", "helloworld"], "result": False},
        {"parameters": ["Hello World", "dlroW olleH"], "result": True},
        {"parameters": ["RaceCar", "raCecaR"], "result": True},
        {"parameters": ["RaceCar", "RaceCar"], "result": False},
        {"parameters": ["Mirror", "rorrim"], "result": False},
        {"parameters": ["Hello World", "dlroW-olleH"], "result": True},
        {"parameters": ["Hello World", "!dlroW !olleH"], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_mirror(test['parameters'][0], test['parameters'][1])
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