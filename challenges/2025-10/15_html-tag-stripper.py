# Daily challenge 2025-10-15: HTML Tag Stripper
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-15
#
# Given a string of HTML code, remove the tags and return the plain text content.
# 
# The input string will contain only valid HTML.
# HTML tags may be nested.
# Remove the tags and any attributes.
# 
# For example, '&#x3C;a href="#">Click here&#x3C;/a>' should return "Click here".

from typing import TypedDict
import re

# Challenge
def strip_tags(html: str) -> str:
    """
    Remove the tags and return the plain text content.
    :param html: The HTML code to be stripped.
    :return: The plain text content of the HTML code.
    """

    return re.sub(r"<.*?>", "", html)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ['<a href="#">Click here</a>'], "result": "Click here"},
        {"parameters": ['<p class="center">Hello <b>World</b>!</p>'], "result": "Hello World!"},
        {"parameters": ['<img src="cat.jpg" alt="Cat">'], "result": ""},
        {"parameters": ['<main id="main"><section class="section">section</section><section class="section">section</section></main>'], "result": "sectionsection"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = strip_tags(test['parameters'][0])
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