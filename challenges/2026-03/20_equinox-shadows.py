# Daily challenge 2026-03-20: Equinox Shadows
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-20
#
# Today is the equinox, when the sun is directly above the equator and perfectly overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.
# 
# The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
# You will only be given a time in 30 minute increments.
# 
# Rules:
# 
# The sun rises at 6am directly "east", and sets at 6pm directly "west".
# A shadow always points opposite the sun.
# The shadow's length (in feet) is the number of hours away from noon, cubed.
# There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.
# 
# Return:
# 
# If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
# Otherwise, return "No shadow".
# 
# For example, given "10:00", return "8ft west" because 10am is 2 hours from noon, so 23 = 8 feet, and the shadow points west because the sun is in the east at 10am.

from typing import TypedDict
from datetime import datetime, timedelta

# Challenge
def get_shadow(time: str) -> str:
    """
    Calculate the shadow length and direction based on the time of day.

    :param time: Time in "HH:MM" format
    :return: A string with the shadow length and direction (e.g., "8ft west"), or "No shadow" if the sun is too high or not present
    """

    # Parse the input time and define noon (12:00) as reference point
    dt = datetime.strptime(time, "%H:%M")
    noon = datetime.strptime("12:00", "%H:%M")

    # Compute the time difference (in hours) relative to noon
    lapsed = dt - noon
    lapsed_hours = lapsed.total_seconds() / 3600
    debug("lapsed hours", lapsed_hours)

    # If the time is too far from noon (more than 6 hours), assume no shadow
    if abs(lapsed_hours) > 6 or lapsed_hours >= 6:
        return "No shadow"

    # Calculate shadow length using a cubic relation (arbitrary model)
    long = abs(lapsed_hours) ** 3
    direction = ""

    # Determine shadow direction based on time of day
    if lapsed_hours < 0:
        direction = "west"   # Morning: shadow points west (sun in the east)
    elif lapsed_hours > 0:
        direction = "east"   # Afternoon: shadow points east (sun in the west)
    else:
        # At exactly noon, there is effectively no shadow
        return "No shadow"

    # Format the result string (remove trailing ".0" for whole numbers)
    result = str(long) + "ft " + direction
    result = result.replace(".0ft", "ft")

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["10:00"], "result": "8ft west"},
        {"parameters": ["15:00"], "result": "27ft east"},
        {"parameters": ["12:00"], "result": "No shadow"},
        {"parameters": ["17:30"], "result": "166.375ft east"},
        {"parameters": ["05:00"], "result": "No shadow"},
        {"parameters": ["06:00"], "result": "216ft west"},
        {"parameters": ["18:00"], "result": "No shadow"},
        {"parameters": ["07:30"], "result": "91.125ft west"},
        {"parameters": ["00:00"], "result": "No shadow"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_shadow(test['parameters'][0])
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