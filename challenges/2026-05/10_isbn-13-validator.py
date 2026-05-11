# Daily challenge 2026-05-10: ISBN-13 Validator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-10
#
# Given a string, determine if it is a valid ISBN-13 number.
# A valid ISBN-13:
# 
# Contains only digits and hyphens
# Has exactly 13 digits after removing hyphens
# Passes the following check:
# 
# Multiply each digit by 1 or 3, alternating (multiply the first digit by 1, the second by 3, the third by 1, and so on).
# The sum of the results must be divisible by 10.
# 
# 
# 

from typing import TypedDict


# Challenge
def is_valid_isbn_13(code: str) -> bool:
    """
    Check if the code is a valid ISBN-13 number.

    :param code: The code to check.
    :return: Returns True if the code is a valid ISBN-13 number, False otherwise.
    """

    # Check if the code contains only digits and hyphens
    if not all(char.isdigit() or char == "-" for char in code):
        debug("ERROR", "The code must contain only digits and hyphens.")
        return False

    # Remove hyphens and convert to a list of digits
    digits = [int(digit) for digit in code.replace("-", "")]

    # Check if the code has exactly 13 digits after removing hyphens
    if len(digits) != 13:
        debug("ERROR", "The code must have exactly 13 digits after removing hyphens.")
        return False

    # Calculate the checksum using alternating weights of 1 and 3
    checksum = sum(digit * (1 if i % 2 == 0 else 3) for i, digit in enumerate(digits))
    if checksum % 10 != 0:
        debug("ERROR", "The checksum is incorrect.")
        return False

    return True


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["9780306406157"], "result": True},
        {"parameters": ["97803064061570"], "result": False},
        {"parameters": ["978-0-13-595705-9"], "result": True},
        {"parameters": ["978-030-64061A-4"], "result": False},
        {"parameters": ["9-7-8-0-1-3-4-7-5-7-5-9-9"], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_valid_isbn_13(test['parameters'][0])
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
