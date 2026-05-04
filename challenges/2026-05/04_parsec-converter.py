# Daily challenge 2026-05-04: Parsec Converter
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-04
#
# In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its equivalent in time or distance.
# 
# If the given integer is odd, it represents time. If it's even, it represents distance.
# 
# Use these conversion rates:
#
# Parsecs
# Time/Distance
# 1, 2 hours
# 2, 6 light years
#
# Return the converted value as an integer.

from typing import TypedDict


# Challenge
def convert_parsecs(parsecs: int) -> int:
    """
    Convert parsecs to time or distance.
    :param parsecs: The number of parsecs.
    :return: Returns the converted value.
    """

    if parsecs % 2 == 0:
        # Even number of parsecs, convert to distance
        return parsecs * 3
    else:
        # Odd number of parsecs, convert to time
        return parsecs * 2


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [1], "result": 2},
        {"parameters": [2], "result": 6},
        {"parameters": [31], "result": 62},
        {"parameters": [88], "result": 264},
        {"parameters": [17], "result": 34},
        {"parameters": [14], "result": 42},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = convert_parsecs(test['parameters'][0])
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