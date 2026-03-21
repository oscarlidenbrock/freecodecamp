# Daily challenge 2025-09-02: RGB to Hex
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-02
#
# Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.
# Here are some example outputs for a given input:
#
# Input                , Output
# "rgb(255, 255, 255)" , "#ffffff"
# "rgb(1, 2, 3)"       , "#010203"
#
# Make any letters lowercase.
# Return a # followed by six characters. Don't use any shorthand values.
#

from typing import TypedDict
import re

# Challenge
def rgb_to_hex(rgb: str) -> str:
    """
    Converts an RGB string (e.g., 'rgb(r, g, b)') into its hexadecimal color representation.

    :param rgb: A string in the format 'rgb(r, g, b)'.
    :return: The hexadecimal color string (e.g., '#rrggbb'), or an empty string if the input is invalid.
    """

    # Extract the integer values for red, green, and blue using regex
    match = re.search(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", rgb)

    if match:
        r, g, b = map(int, match.groups())

        # Format each component as a two-digit hexadecimal and combine them
        return f"#{r:02x}{g:02x}{b:02x}"

    # Return an empty string if the input does not match the expected format
    return ""

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["rgb(255, 255, 255)"], "result": "#ffffff"},
        {"parameters": ["rgb(1, 11, 111)"], "result": "#010b6f"},
        {"parameters": ["rgb(173, 216, 230)"], "result": "#add8e6"},
        {"parameters": ["rgb(79, 123, 201)"], "result": "#4f7bc9"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = rgb_to_hex(test['parameters'][0])
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