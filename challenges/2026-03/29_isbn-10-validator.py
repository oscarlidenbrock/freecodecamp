# Daily challenge 2026-03-29: ISBN-10 Validator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-29
#
# Given a string, determine if it's a valid ISBN-10.
# An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):
# 
# The first 9 characters must be digits, and
# The final character may be a digit or the letter "X", which represents the number 10.
# 
# To validate it:
# 
# Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
# Add all the results together.
# If the total is divisible by 11, it's valid.
# 

from typing import TypedDict
import re

# Challenge
def is_valid_isbn10(isbn: str):
    """
    Validate an ISBN-10 identifier.

    :param isbn: ISBN string (may include hyphens)
    :return: True if the ISBN-10 is valid, otherwise False
    """

    # Remove hyphens to normalize the input
    code = isbn.replace("-", "")

    # Validate format:
    # - Exactly 10 characters
    # - First 9 must be digits
    # - Last character must be a digit or 'X' (checksum value 10)
    if not bool(re.match(r'^[0-9]{9}[X0-9]$', code)):
        return False

    # Compute the ISBN-10 checksum:
    # Each digit is multiplied by its 1-based position index
    sum = 0

    for i in range(len(code)):
        char = code[i]

        # 'X' represents the value 10 in the checksum calculation
        if char == "X":
            sum += 10 * (i + 1)
        else:
            sum += int(char) * (i + 1)

    # A valid ISBN-10 must have a checksum divisible by 11
    return sum % 11 == 0

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["0-306-40615-2"], "result": True},
        {"parameters": ["0-306-40615-1"], "result": False},
        {"parameters": ["0-8044-2957-X"], "result": True},
        {"parameters": ["X-306-40615-2"], "result": False},
        {"parameters": ["0-6822-2589-4"], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_valid_isbn10(test['parameters'][0])
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