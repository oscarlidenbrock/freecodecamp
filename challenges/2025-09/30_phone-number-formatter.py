# Daily challenge 2025-09-30: Phone Number Formatter
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-30
#
# Given a string of eleven digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".

from typing import TypedDict


# Challenge
def format_number(number: str) -> str:
    """
    Format a numeric string into a standardized phone number.

    Expected input format:
    - A string of digits with at least 11 characters
      (e.g., "05552340182")

    Output format:
    - +<country_code> (<area_code>) <prefix>-<line_number>
      (e.g., "+0 (555) 234-0182")

    :param number: String containing only digits
    :return: Formatted phone number string
    """

    # Extract and format each part of the phone number using slicing
    return f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:11]}"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["05552340182"], "result": "+0 (555) 234-0182"},
        {"parameters": ["15554354792"], "result": "+1 (555) 435-4792"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = format_number(test['parameters'][0])
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