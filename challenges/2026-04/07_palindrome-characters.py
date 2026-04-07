# Daily challenge 2026-04-07: Palindrome Characters
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-07
#
# Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).
# 
# A palindrome is a string that is the same forward and backward.
# If it's not a palindrome, return "none".
# 

from typing import TypedDict


# Challenge
def palindrome_locator(text: str) -> str:
    """
    Check whether a string is a palindrome. If it is, return its middle
    character (odd length) or the two middle characters (even length).
    Otherwise, return "none".

    :param text: Input string to evaluate
    :return: Middle character(s) if palindrome, otherwise "none"
    """

    # Compute half length (used to split the string)
    text_len = len(text) // 2

    # Extract left half and reversed right half for comparison
    text_left = text[:text_len]
    text_right = text[-text_len:][::-1]

    # Compare halves to determine if the string is a palindrome
    if text_left == text_right:
        # Return middle character(s) depending on string length parity
        if len(text) % 2 == 0:
            return text[text_len - 1:text_len + 1]
        else:
            return text[text_len]

    # Not a palindrome
    return "none"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["racecar"], "result": "e"},
        {"parameters": ["level"], "result": "v"},
        {"parameters": ["freecodecamp"], "result": "none"},
        {"parameters": ["noon"], "result": "oo"},
        {"parameters": ["11100111"], "result": "00"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = palindrome_locator(test['parameters'][0])
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