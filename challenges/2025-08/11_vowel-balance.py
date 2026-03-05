# Daily challenge 2025-08-11: Vowel Balance
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-11
#
# Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.
# 
# The string can contain any characters.
# The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
# If there's an odd number of characters in the string, ignore the center character.
# 

from typing import TypedDict


# Challenge
def is_balanced(input: str) -> bool:
    """
    Returns whether the input string is balanced (same number of vowels in both halves of the string).

    :param input: The string to check.
    :return: True if the string is balanced, False otherwise.
    """
    result = False

    # Get both halves of the string
    left, right = input[:len(input) // 2], input[len(input) // 2:]

    # Adjust halves if the string length is odd
    if len(left) > len(right): left = left[-1:]
    if len(left) < len(right): right = right[1:]

    # Count vowels in both halves of the string
    count_left = sum(1 for c in left.lower() if c in "aeiou")
    count_right = sum(1 for c in right.lower() if c in "aeiou")

    # If both halves have the same number of vowels, the string is balanced
    if count_left == count_right: result = True

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["racecar"], "result": True},
        {"parameters": ["Lorem Ipsum"], "result": True},
        {"parameters": ["Kitty Ipsum"], "result": False},
        {"parameters": ["string"], "result": False},
        {"parameters": [" "], "result": True},
        {"parameters": ["abcdefghijklmnopqrstuvwxyz"], "result": False},
        {"parameters": ["123A#b!E&*456-o.U"], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if is_balanced(test['parameters'][0]) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")

test()