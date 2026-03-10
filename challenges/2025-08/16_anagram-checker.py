# Daily challenge 2025-08-16: Anagram Checker
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-16
#
# Given two strings, determine if they are anagrams of each other (contain the same characters in any order).
# 
# Ignore casing and white space.
# 

from typing import TypedDict


# Challenge
def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if both strings are anagrams.
    :param str1: First string
    :param str2: Second string
    :return: True if both strings are anagrams, otherwise False
    """
    result = True

    # Count each character in str1
    for char in str1:
        # Compare how many times this character appears in both strings.
        # If the counts are different, they cannot be anagrams.
        if str1.lower().count(char) != str2.lower().count(char):
            return False

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["listen", "silent"], "result": True},
        {"parameters": ["School master", "The classroom"], "result": True},
        {"parameters": ["A gentleman", "Elegant man"], "result": True},
        {"parameters": ["Hello", "World"], "result": False},
        {"parameters": ["apple", "banana"], "result": False},
        {"parameters": ["cat", "dog"], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = are_anagrams(test['parameters'][0], test['parameters'][1])
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