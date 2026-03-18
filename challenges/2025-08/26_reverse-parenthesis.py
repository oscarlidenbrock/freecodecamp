# Daily challenge 2025-08-26: Reverse Parenthesis
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-26
#
# Given a string that contains properly nested parentheses, return the decoded version of the string using the following rules:
# 
# All characters inside each pair of parentheses should be reversed.
# Parentheses should be removed from the final result.
# If parentheses are nested, the innermost pair should be reversed first, and then its result should be included in the reversal of the outer pair.
# Assume all parentheses are evenly balanced and correctly nested.
# 

from typing import TypedDict
import re

# Challenge
def decode(input: str) -> str:
    """
    Decode a string by reversing the content inside parentheses.
    Nested parentheses are resolved from the innermost to the outermost.

    :param input: The string to decode
    :return: The decoded string
    """

    # Continue processing while there are parentheses in the string
    while '(' in input:
        # Find all substrings enclosed in non-nested parentheses (innermost groups)
        matches = re.findall(r'\(([^()]*)\)', input)

        # Reverse each match and replace it (including its parentheses) in the string
        for match in matches:
            input = input.replace(f'({match})', match[::-1])

    # Return the fully decoded string
    return input

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["(f(b(dc)e)a)"], "result": "abcdef"},
        {"parameters": ["((is?)(a(t d)h)e(n y( uo)r)aC)"], "result": "Can you read this?"},
        {"parameters": ["f(Ce(re))o((e(aC)m)d)p"], "result": "freeCodeCamp"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = decode(test['parameters'][0])
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