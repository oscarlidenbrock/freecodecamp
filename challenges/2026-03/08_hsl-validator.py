# Daily challenge 2026-03-08: HSL Validator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-08
#
# Given a string, determine whether it is a valid CSS hsl() color value.
# 
# 
# A valid HSL value must be in the format "hsl(h, s%, l%)", where:
# 
# h (hue) must be a number between 0 and 360 (inclusive).
# s (saturation) must be a percentage between 0% and 100%.
# l (lightness) must be a percentage between 0% and 100%.
# 
# 
# 
# Spaces are only allowed:
# 
# After the opening parenthesis
# Before and/or after the commas
# Before and/or after closing parenthesis
# 
# 
# 
# Optionally, the value can end with a semi-colon (";").
# 
# 
# For example, "hsl(240, 50%, 50%)" is a valid HSL value.

from typing import TypedDict
import re

# Challenge
def is_valid_hsl(hsl: str) -> bool:
    """
    Check whether the given string contains a valid CSS hsl() function.

    :param hsl: The HSL function as a string.
    :return: True if the HSL value is valid, otherwise False.
    """

    # Extract HSL values
    match = re.search(r'hsl\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)\s*;?', hsl)

    if match:
        hue = int(match.group(1))
        saturation = int(match.group(2))
        lightness = int(match.group(3))

        debug("hue", hue)
        debug("saturation", saturation)
        debug("lightness", lightness)

        # Validate hue
        if hue < 0 or hue > 360:
            debug("incorrect hue", hue)
            return False

        # Validate saturation
        if saturation < 0 or saturation > 100:
            debug("incorrect saturation", saturation)
            return False

        # Validate lightness
        if lightness < 0 or lightness > 100:
            debug("incorrect lightness", lightness)
            return False

        # Value is valid
        return True

    return False

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["hsl(240, 50%, 50%)"], "result": True},
        {"parameters": ["hsl( 200 , 50% , 75% )"], "result": True},
        {"parameters": ["hsl(99,60%,80%);"], "result": True},
        {"parameters": ["hsl(0, 0%, 0%) ;"], "result": True},
        {"parameters": ["hsl(  10  ,  20%   ,  30%   )    ;"], "result": True},
        {"parameters": ["hsl(361, 50%, 80%)"], "result": False},
        {"parameters": ["hsl(300, 101%, 70%)"], "result": False},
        {"parameters": ["hsl(200, 55%, 75)"], "result": False},
        {"parameters": ["hsl (80, 20%, 10%)"], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_valid_hsl(test['parameters'][0])
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