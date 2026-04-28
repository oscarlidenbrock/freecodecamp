# Daily challenge 2025-10-19: HTML Attribute Extractor
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-19
#
# Given a string of a valid HTML element, return the attributes of the element using the following criteria:
# 
# You will only be given one element.
# Attributes will be in the format: attribute="value".
# Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
# Return attributes in the order they are given.
# If no attributes are found, return an empty array.
# 

from typing import TypedDict
import re

# Challenge
def extract_attributes(element: str) -> list[str]:
    """
    Given a string of a valid HTML element, return the attributes of the element.
    :param element: The HTML element string.
    :return: The attributes of the element.
    """

    # Find all attributes in the element.
    attrs = re.findall(
        r'''([^\s=\/<>]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'=<>`]+)))?''',
        element
    )

    # Format the attributes into a list of strings.
    result = []
    for i, attr in enumerate(attrs):
        # If the attribute value is not empty, add it to the result.
        if not attr[1] == "":
            result.append(attr[0] + ", " + attr[1])

    # Return the formatted attributes.
    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": ['<span class="red"></span>'], "result": ["class, red"]},
        {"parameters": ['<meta charset="UTF-8" />'], "result": ["charset, UTF-8"]},
        {"parameters": ["<p>Lorem ipsum dolor sit amet</p>"], "result": []},
        {"parameters": ['<input name="email" type="email" required="true" />'], "result": ["name, email", "type, email", "required, true"]},
        {"parameters": ['<button id="submit" class="btn btn-primary">Submit</button>'], "result": ["id, submit", "class, btn btn-primary"]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = extract_attributes(test['parameters'][0])
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