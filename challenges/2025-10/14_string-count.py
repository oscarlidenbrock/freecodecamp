# Daily challenge 2025-10-14: String Count
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-14
#
# Given two strings, determine how many times the second string appears in the first.
# 
# The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.
# 

from typing import TypedDict
import re

# Challenge
def count(text: str, parameter: str) -> int:
    """
    Return how many times the parameter string appears in the text.
    :param text: The text to search in.
    :param parameter: The string to search for.
    :return: How many times the parameter string appears in the text.
    """

    # Track how many matching slices we find while scanning the text.
    count = 0

    for i in range(len(text)):
        # Build the end index for a slice that starts at the current position
        # and has the same length as the search string.
        l = len(parameter) + i

        # Compare the current slice against the parameter and count it when it
        # matches. Advancing one character at a time allows overlapping matches.
        if l <= len(text) and text[i:l] == parameter:
            count += 1

    return count

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": ['abcdefg', 'def'], "result": 1},
        {"parameters": ['hello', 'world'], "result": 0},
        {"parameters": ['mississippi', 'iss'], "result": 2},
        {"parameters": ['she sells seashells by the seashore', 'sh'], "result": 3},
        {"parameters": ['101010101010101010101', '101'], "result": 10},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = count(test['parameters'][0], test['parameters'][1])
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
