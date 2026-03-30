# Daily challenge 2026-03-30: Due Date
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-30
#
# Given a date string, return the date 9 months in the future.
# 
# The given and return strings have the format "YYYY-MM-DD".
# If the month nine months into the future doesn't contain the original day number, return the last day of that month.
# 

from typing import TypedDict
import calendar

# Challenge
def get_due_date(date_str: str) -> str:
    """
    Calculate the date exactly 9 months after a given date.

    :param date_str: Date string in 'YYYY-MM-DD' format
    :return: Date string 'YYYY-MM-DD' that is 9 months in the future
    """

    # Split the input date into [year, month, day]
    segments = date_str.split('-')

    # Add 9 months to the current month
    segments[1] = int(segments[1]) + 9

    # If the resulting month exceeds 12, wrap around and increment the year
    if segments[1] > 12:
        segments[1] -= 12
        segments[0] = str(int(segments[0]) + 1)

    # Determine the last valid day of the target month
    last_day = calendar.monthrange(int(segments[0]), segments[1])[1]
    debug("last month day", last_day)

    # Adjust the day if the original day exceeds the last day of the target month
    if int(segments[2]) > last_day:
        segments[2] = str(last_day)

    # Format the month as a 2-digit string (e.g., '03', '12')
    segments[1] = str(segments[1]).zfill(2)

    # Reconstruct the final date string
    result = "-".join(segments)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["2025-03-30"], "result": "2025-12-30"},
        {"parameters": ["2025-04-27"], "result": "2026-01-27"},
        {"parameters": ["2025-05-29"], "result": "2026-02-28"},
        {"parameters": ["2026-06-30"], "result": "2027-03-30"},
        {"parameters": ["2026-10-11"], "result": "2027-07-11"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_due_date(test['parameters'][0])
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