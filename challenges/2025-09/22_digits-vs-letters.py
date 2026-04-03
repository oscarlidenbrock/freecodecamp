# Daily challenge 2025-09-22: Digits vs Letters
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-22
#
# Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.
# 
# Digits consist of 0-9.
# Letters consist of a-z in upper or lower case.
# Ignore any other characters.
# 

from typing import TypedDict


# Challenge
def digits_or_letters(text: str) -> str:
    """
    Determines whether a string contains more alphabetic characters or numeric digits.

    Only ASCII letters (a–z) and digits (0–9) are considered.
    All other characters (spaces, symbols, punctuation, etc.) are ignored.

    :param text: Input string to analyze
    :return:
        - "letters" if alphabetic characters are more frequent
        - "digits" if numeric digits are more frequent
        - "tie" if both counts are equal
    """

    count_digits = 0
    count_letters = 0

    for char in text:
        # Count ASCII letters (case-insensitive)
        if "a" <= char.lower() <= "z":
            count_letters += 1
        # Count numeric digits
        elif "0" <= char <= "9":
            count_digits += 1

    # Compare counts to determine the dominant character type
    if count_letters > count_digits:
        return "letters"
    elif count_digits > count_letters:
        return "digits"
    else:
        return "tie"


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["abc123"], "result": "tie"},
        {"parameters": ["a1b2c3d"], "result": "letters"},
        {"parameters": ["1a2b3c4"], "result": "digits"},
        {"parameters": ["abc123!@#DEF"], "result": "letters"},
        {"parameters": ["H3110 W0R1D"], "result": "digits"},
        {"parameters": ["P455W0RD"], "result": "tie"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = digits_or_letters(test['parameters'][0])
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