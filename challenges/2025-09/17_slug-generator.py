# Daily challenge 2025-09-17: Slug Generator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-17
#
# Given a string, return a URL-friendly version of the string using the following constraints:
# 
# All letters should be lowercase.
# All characters that are not letters, numbers, or spaces should be removed.
# All spaces should be replaced with the URL-encoded space code %20.
# Consecutive spaces should be replaced with a single %20.
# The returned string should not have leading or trailing %20.
# 

from typing import TypedDict
import re

# Challenge
def generate_slug(text: str) -> str:
    """
    Generates a URL-safe slug from a given text string.

    :param text: Input string to be transformed
    :return: URL-encoded slug
    """

    # Normalize case and remove leading/trailing whitespace
    slug = text.lower().strip()

    # Remove any character that is not a lowercase letter, digit, or space
    slug = re.sub(r'[^a-z0-9 ]', '', slug)

    # Collapse consecutive spaces into a single space
    while "  " in slug:
        slug = slug.replace("  ", " ")

    # Replace spaces with URL-encoded representation
    slug = slug.replace(" ", "%20")

    return slug

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["helloWorld"], "result": "helloworld"},
        {"parameters": ["hello world!"], "result": "hello%20world"},
        {"parameters": [" hello-world "], "result": "helloworld"},
        {"parameters": ["hello  world"], "result": "hello%20world"},
        {"parameters": ["  ?H^3-1*1]0! W[0%R#1]D  "], "result": "h3110%20w0r1d"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = generate_slug(test['parameters'][0])
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