# Daily challenge 2026-03-25: Cooldown Time
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-25
#
# Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.
# 
# Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
# A user must wait at least 48 hours before retaking an exam.
# 

from typing import TypedDict
from datetime import datetime

def can_retake(finish_time: str, current_time: str) -> bool:
    """
    Determine whether a user is allowed to retake an exam based on the time
    elapsed since their last attempt.

    Both input values must be datetime strings in ISO 8601 format:
    "YYYY-MM-DDTHH:MM:SS".

    The user can retake the exam only if at least 48 hours have passed
    since the previous attempt.

    :param finish_time: Datetime when the previous exam attempt ended
    :param current_time: Current datetime
    :return: True if 48 hours or more have passed, otherwise False
    """

    # Expected datetime format (ISO 8601 without timezone)
    dt_format = "%Y-%m-%dT%H:%M:%S"

    # Convert input strings to datetime objects
    dt_finish = datetime.strptime(finish_time, dt_format)
    dt_current = datetime.strptime(current_time, dt_format)

    # Compute time difference between current time and last attempt
    dt_difference = dt_current - dt_finish
    debug("datetime difference", dt_difference.days)

    # Check if at least 48 hours (2 days) have elapsed
    return dt_difference.days >= 2

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["2026-03-23T08:00:00", "2026-03-25T14:00:00"], "result": True},
        {"parameters": ["2026-03-24T14:00:00", "2026-03-25T10:00:00"], "result": False},
        {"parameters": ["2026-03-23T09:25:00", "2026-03-25T09:25:00"], "result": True},
        {"parameters": ["2026-03-25T11:50:00", "2026-03-23T11:49:59"], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = can_retake(test['parameters'][0], test['parameters'][1])
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