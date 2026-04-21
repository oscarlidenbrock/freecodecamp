# Daily challenge 2025-10-11: Hex to Decimal
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-11
#
# Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.
# Hexadecimal is a number system that uses 16 digits:
# 
# 0-9 represent values 0 through 9.
# A-F represent values 10 through 15.
# 
# Here's a partial conversion table:
# 
# Hexadecimal , Decimal
# 0           , 0
# 1           , 1
# ...         , ...
# 9           , 9
# A           , 10
# ...         , ...
# F           , 15
# 10          , 16
# ...         , ...
# 9F          , 159
# A0          , 160
# ...         , ...
# FF          , 255
# 100         , 256
#
# The string will only contain characters 0–9 and A–F.
# 

from typing import TypedDict


# Challenge
def hex_to_decimal(hex: str) -> int:
    """
    Convert a hexadecimal string to its decimal equivalent.
    :param hex: The hexadecimal string to convert.
    :return: The decimal equivalent of the hexadecimal string.
    """

    return int(hex, 16)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": ["A"], "result": 10},
        {"parameters": ["15"], "result": 21},
        {"parameters": ["2E"], "result": 46},
        {"parameters": ["FF"], "result": 255},
        {"parameters": ["A3F"], "result": 2623},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = hex_to_decimal(test['parameters'][0])
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