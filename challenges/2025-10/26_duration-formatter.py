# Daily challenge 2025-10-26: Duration Formatter
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-26
#
# Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:
# 
# Seconds: Should always be two digits.
# Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
# Hours: Should be included only if they're greater than zero.
# 

from typing import TypedDict


# Challenge
def format(seconds: int) -> str:
    """
    Return the time in the format "H:MM:SS".
    :param seconds: The seconds.
    :return: Returns the time in the format "H:MM:SS".
    """

    minutes = seconds // 60
    hours = minutes // 60
    minutes = minutes % 60
    seconds = seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes}:{seconds:02d}"


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [500], "result": "8:20"},
        {"parameters": [4000], "result": "1:06:40"},
        {"parameters": [1], "result": "0:01"},
        {"parameters": [5555], "result": "1:32:35"},
        {"parameters": [99999], "result": "27:46:39"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = format(test['parameters'][0])
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