# Daily challenge 2026-04-06: What Day Is It?
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-06
#
# Given a Unix timestamp in milliseconds, return the day of the week.
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
def get_day_of_week(timestamp: int) -> str:
    """
    Get the week day from a timestamp
    :param timestamp: The timestamp
    :return: The week day relative to the timestamp
    """

    # Get the miliseconds
    ms = timestamp / 1000

    # Transform timestamp in a datetime object
    date = datetime.fromtimestamp(ms)

    # Return the day of the week from datetime
    return date.strftime("%A")

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [1775492249000], "result": "Monday"},
        {"parameters": [1766246400000], "result": "Saturday"},
        #{"parameters": [33791256000000], "result": "Tuesday"},
        {"parameters": [1773576000000], "result": "Sunday"},
        {"parameters": [0], "result": "Thursday"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_day_of_week(test['parameters'][0])
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