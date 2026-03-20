# Daily challenge 2025-08-31: Hex Generator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-31
#
# Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.
# 
# The function should handle "red", "green", or "blue" as an input argument.
# If the input is not one of those, the function should return "Invalid color".
# The function should return a random six-character hex color code where the input color value is greater than any of the others.
# Example of valid outputs for a given input:
#
# Input  , Output
# "red"  , "FF0000"
# "green", "00FF00"
# "blue" , "0000FF"
# 

from typing import TypedDict
import random

# Challenge
def generate_hex(color: str) -> str:
    """
    Return a hexadecimal color code with a given Red/Green/Blue dominant color
    :param color: The dominant color
    :return: the hexadecimal color
    """

    result = ""

    match color:
        case "red":
            # Set red color in random value from 1 to 255
            random_color = random.randint(1, 255)
            result = str(hex(random_color)[2:]) + "0000"
        case "green":
            # Set green color in random value from 1 to 255
            random_color = random.randint(1, 255)
            result = "00" + str(hex(random_color)[2:]) + "00"
        case "blue":
            # Set blue color in random value from 1 to 255
            random_color = random.randint(1, 255)
            result = "0000" + str(hex(random_color)[2:])
        case _:
            # Otherwise, return "Invalid color"
            return "Invalid color"

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["yellow"], "result": "Invalid color"}
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = generate_hex(test['parameters'][0])
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