# Daily challenge 2025-09-07: Roman Numeral Parser
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-07
#
# Given a string representing a Roman numeral, return its integer value.
# Roman numerals consist of the following symbols and values:
# 
# Symbol, Value
# I,      1
# V,      5
# X,      10
# L,      50
# C,      100
# D,      500
# M,      1000
#
# Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise, values are added.
# 

from typing import TypedDict


# Challenge
def parse_roman_numeral(numeral: str) -> int:
    """
    Converts a Roman numeral string into its integer value.

    :param numeral: Roman numeral string (e.g., "XIV")
    :return: Integer representation of the numeral
    """

    result = 0

    # Mapping of Roman numerals:
    # Each entry contains: [order_position, numeric_value]
    # The position is used to determine subtraction cases
    roman_values = {
        "I": [1, 1],
        "V": [2, 5],
        "X": [3, 10],
        "L": [4, 50],
        "C": [5, 100],
        "D": [6, 500],
        "M": [7, 1000]
    }

    # Iterate through each character in the numeral
    for i in range(len(numeral)):
        char = numeral[i]
        position, value = roman_values[char]

        # Check if there is a next character to compare with
        if i < len(numeral) - 1:
            next_char = numeral[i + 1]
            next_position = roman_values[next_char][0]

            # If current symbol has lower rank than the next one,
            # it should be subtracted (e.g., I before V or X)
            if position < next_position:
                debug("rest " + char, value)
                result -= value
            else:
                # Otherwise, add the value normally
                debug("sum " + char, value)
                result += value
        else:
            # Last character is always added
            debug("sum " + char, value)
            result += value

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": ["III"], "result": 3},
        {"parameters": ["IV"], "result": 4},
        {"parameters": ["XXVI"], "result": 26},
        {"parameters": ["XCIX"], "result": 99},
        {"parameters": ["CDLX"], "result": 460},
        {"parameters": ["DIV"], "result": 504},
        {"parameters": ["MMXXV"], "result": 2025},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = parse_roman_numeral(test['parameters'][0])
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