# Daily challenge 2025-10-17: Credit Card Masker
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-17
#
# Given a string of credit card numbers, return a masked version of it using the following constraints:
# 
# The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
# Replace all numbers, except the last four, with an asterisk (*).
# Leave the remaining characters unchanged.
# 
# For example, given "4012-8888-8888-1881" return "****-****-****-1881".

from typing import TypedDict


# Challenge
def mask(card: str) -> str:
    """
    Return a masked version of the credit card number.
    :param card: The credit card number.
    :return: The masked credit card number.
    """

    # Get the separator character
    separator = " "

    for i in range(len(card)):
        if not card[i].isdigit():
            separator = card[i]
            break

    # Split the card number into segments based on spaces or hyphens
    segments = card.split(separator)

    # Replace all but the last four digits with asterisks
    for i in range(len(segments) - 1):
        segments[i] = "*" * len(segments[i])

    return separator.join(segments)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["4012-8888-8888-1881"], "result": "****-****-****-1881"},
        {"parameters": ["5105 1051 0510 5100"], "result": "**** **** **** 5100"},
        {"parameters": ["6011 1111 1111 1117"], "result": "**** **** **** 1117"},
        {"parameters": ["2223-0000-4845-0010"], "result": "****-****-****-0010"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = mask(test['parameters'][0])
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