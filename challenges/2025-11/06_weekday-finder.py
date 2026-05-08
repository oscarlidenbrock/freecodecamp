# Daily challenge 2025-11-06: Weekday Finder
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-06
#
# Given a string date in the format YYYY-MM-DD, return the day of the week.
# Valid return days are:
# 
# "Sunday"
# "Monday"
# "Tuesday"
# "Wednesday"
# "Thursday"
# "Friday"
# "Saturday"
# 
# Be sure to ignore time zones.

from typing import TypedDict
from datetime import datetime

# Challenge
def get_weekday(date_string):
    """
    Return the day of the week for a given date string.

    :param date_string: A valid date string in the format YYYY-MM-DD.
    :return: The day of the week as a string.
    """

    date_dt = datetime.strptime(date_string, "%Y-%m-%d")
    return date_dt.strftime("%A")

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["2025-11-06"], "result": "Thursday"},
        {"parameters": ["1999-12-31"], "result": "Friday"},
        {"parameters": ["1111-11-11"], "result": "Saturday"},
        {"parameters": ["2112-12-21"], "result": "Wednesday"},
        {"parameters": ["2345-10-01"], "result": "Monday"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_weekday(test['parameters'][0])
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