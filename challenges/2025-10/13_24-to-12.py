# Daily challenge 2025-10-13: 24 to 12
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-13
#
# Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".
# 
# The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
# 

from typing import TypedDict


# Challenge
def to_12(time: str) -> str:
    """
    Convert 24-hour time to 12-hour time.
    :param time: 12-hour time string.
    :return: 24-hour time string.
    """

    # Parse the HHMM string into numeric hour and minute components.
    hour = int(time[:2])
    minute = int(time[2:])
    period = "AM"

    if hour == 0:
        # Midnight uses 12 instead of 0 in 12-hour notation.
        hour = 12
    elif hour == 12:
        # Noon stays at 12 and switches to PM.
        period = "PM"
    elif hour > 12:
        # Afternoon hours wrap into the 1-11 range and use PM.
        hour -= 12
        period = "PM"

    # Build the output with an unpadded hour and a two-digit minute.
    result = f"{hour}:{minute:02d} {period}"

    return result


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["1124"], "result": "11:24 AM"},
        {"parameters": ["0900"], "result": "9:00 AM"},
        {"parameters": ["1455"], "result": "2:55 PM"},
        {"parameters": ["2346"], "result": "11:46 PM"},
        {"parameters": ["0030"], "result": "12:30 AM"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = to_12(test['parameters'][0])
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
