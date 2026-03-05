# Daily challenge 2025-08-12: Base Check
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-12
#
# Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.
# 
# The string may contain integers, and uppercase or lowercase characters.
# The check should be case-insensitive.
# The base can be any number 2-36.
# A number is valid if every character is a valid digit in the given base.
# Example of valid digits for bases:
# 
# Base 2: 0-1
# Base 8: 0-7
# Base 10: 0-9
# Base 16: 0-9 and A-F
# Base 36: 0-9 and A-Z
# 
# 
# 

from typing import TypedDict


# Challenge
def is_valid_number(value: str, base: int) -> bool:
    """
    Check whether a string represents a valid number in the specified base.

    :param value: The string to validate.
    :param base: The numeric base used for validation.
    :return: True if the string is a valid number in the given base, False otherwise.
    """
    try:
        int(value, base)
        return True
    except ValueError:
        return False

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["10101", 2], "result": True},
        {"parameters": ["10201", 2], "result": False},
        {"parameters": ["76543210", 8], "result": True},
        {"parameters": ["9876543210", 8], "result": False},
        {"parameters": ["9876543210", 10], "result": True},
        {"parameters": ["ABC", 10], "result": False},
        {"parameters": ["ABC", 16], "result": True},
        {"parameters": ["Z", 36], "result": True},
        {"parameters": ["ABC", 20], "result": True},
        {"parameters": ["4B4BA9", 16], "result": True},
        {"parameters": ["5G3F8F", 16], "result": False},
        {"parameters": ["5G3F8F", 17], "result": True},
        {"parameters": ["abc", 10], "result": False},
        {"parameters": ["abc", 16], "result": True},
        {"parameters": ["AbC", 16], "result": True},
        {"parameters": ["z", 36], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if is_valid_number(test['parameters'][0], test['parameters'][1]) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")

test()