# Daily challenge 2025-11-14: Is It the Weekend?
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-14
#
# Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.
# 
# The weekend starts on Saturday.
# If the given date is Saturday or Sunday, return "It's the weekend!".
# Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
# If X is 1, use "day" (singular) instead of "days" (plural).
# Make sure the calculation ignores your local timezone.
# 

from datetime import date
from typing import TypedDict


# Challenge
def days_until_weekend(date_string: str) -> str:
    """
    Get the number of days left until the weekend.

    :param date_string: A string representing a date in the format "YYYY-MM-DD".
    :return: Returns the number of days left until the weekend.
    """

    current_date = date.fromisoformat(date_string)
    days_left = 5 - current_date.weekday()

    if days_left <= 0:
        return "It's the weekend!"

    unit = "day" if days_left == 1 else "days"
    return f"{days_left} {unit} until the weekend."

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["2025-11-14"], "result": "1 day until the weekend."},
        {"parameters": ["2025-01-01"], "result": "3 days until the weekend."},
        {"parameters": ["2025-12-06"], "result": "It's the weekend!"},
        {"parameters": ["2026-01-27"], "result": "4 days until the weekend."},
        {"parameters": ["2026-09-07"], "result": "5 days until the weekend."},
        {"parameters": ["2026-11-29"], "result": "It's the weekend!"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = days_until_weekend(test['parameters'][0])
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
