# Daily challenge 2025-10-09: Space Week Day 6: Moon Phase
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-09
#
# For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:
# Use a simplified lunar cycle of 28 days, divided into four equal phases:
# 
# "New": days 1 - 7
# "Waxing": days 8 - 14
# "Full": days 15 - 21
# "Waning": days 22 - 28
# 
# After day 28, the cycle repeats with day 1, a new moon.
# 
# Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
# You will not be given any dates before the reference date.
# Return the correct phase as a string.
# 
# Note: Day 1 represents the day of the new moon, meaning 0 days have passed since the last new moon.

from typing import TypedDict
from datetime import datetime

# Challenge
def moon_phase(date_string: str) -> str:
    """
    Determine the phase of the moon for a given date.

    :param date_string: A date string in the format YYYY-MM-DD
    :return: The phase of the moon as a string
    """

    date_from = datetime.strptime("2000-01-06", "%Y-%m-%d")
    date_to = datetime.strptime(date_string, "%Y-%m-%d")

    # Count how many full days have elapsed since the reference new moon.
    date_diff = date_to - date_from

    # Map the elapsed days into the repeating 28-day lunar cycle.
    days_since_new_moon = date_diff.days % 28

    # Each phase covers a 7-day block within the simplified cycle.
    if days_since_new_moon < 7:
        return "New"
    elif days_since_new_moon < 14:
        return "Waxing"
    elif days_since_new_moon < 21:
        return "Full"
    else:
        return "Waning"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["2000-01-12"], "result": "New"},
        {"parameters": ["2000-01-13"], "result": "Waxing"},
        {"parameters": ["2014-10-15"], "result": "Full"},
        {"parameters": ["2012-10-21"], "result": "Waning"},
        {"parameters": ["2022-12-14"], "result": "New"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = moon_phase(test['parameters'][0])
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
