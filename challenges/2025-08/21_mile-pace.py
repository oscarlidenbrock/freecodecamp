# Daily challenge 2025-08-21: Mile Pace
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-21
#
# Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the average time it took to run each mile in the format "MM:SS".
# 
# Add leading zeros when needed.
# 

from typing import TypedDict


# Challenge
def mile_pace(miles: float, duration: str):
    """
    Calculate the average time per mile for a run.

    :param miles: total distance in miles
    :param duration: total duration of the run in "MM:SS" format
    :return: average time per mile as a string in "MM:SS" format
    """

    result = ""

    # Convert duration from "MM:SS" string to total seconds
    duration_minutes, duration_seconds = duration.split(":")
    seconds = int(duration_minutes) * 60 + int(duration_seconds)

    # Calculate minutes and seconds per mile
    minutes_per_mile = int((seconds / miles) // 60)
    seconds_per_mile = int((seconds / miles) % 60)

    debug("minutes_per_mile", minutes_per_mile)
    debug("seconds_per_mile", seconds_per_mile)

    # Format the pace as a string in "MM:SS" format
    result = f"{minutes_per_mile:02d}:{seconds_per_mile:02d}"

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [3, "24:00"], "result": "08:00"},
        {"parameters": [1, "06:45"], "result": "06:45"},
        {"parameters": [2, "07:00"], "result": "03:30"},
        {"parameters": [26.2, "120:35"], "result": "04:36"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = mile_pace(test['parameters'][0], test['parameters'][1])
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