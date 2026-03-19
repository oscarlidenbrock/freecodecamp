# Daily challenge 2026-03-18: Largest Number
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-18
#
# Given a string of numbers separated by various punctuation, return the largest number.
# 
# The given string will only contain numbers and separators.
# Separators can be commas (","), exclamation points ("!"), question marks ("?"), colons (":"), or semi-colons (";").
# 

from typing import TypedDict
import re

# Challenge
def largest_number(input: str) -> float:
    """
    Extract all numeric values (integers and floats, including negatives)
    from the input string and return the largest one.

    :param input: String containing numbers separated by arbitrary characters
    :return: The largest number found in the string as a float
    """

    # Extract all numbers from the string (supports integers, floats, and negatives)
    numbers = re.findall(r'-?\d+\.\d+|-?\d+', input)

    # Convert extracted values from strings to floats
    numbers = [float(n) for n in numbers]
    debug("numbers", numbers)

    # Return the maximum value found
    return max(numbers)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": ["1,2"], "result": 2},
        {"parameters": ["4;15:60,26?52!0"], "result": 60},
        {"parameters": ["-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011"], "result": -402},
        {"parameters": ["12;-50,99.9,49.1!-10.1?88?16"], "result": 99.9},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = largest_number(test['parameters'][0])
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