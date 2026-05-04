# Daily challenge 2026-05-03: Good Day
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-03
#
# Given a time string in "HH:MM" format (24-hour clock), return:
# 
# "Good morning" for times 05:00 to 11:59
# "Good afternoon" for times 12:00 to 17:59
# "Good evening" for times 18:00 to 21:59
# "Good night" for times 22:00 to 04:59
# 

from typing import TypedDict


# Challenge
def get_greeting(hour: str) -> str:
    """
    Return the appropriate greeting based on the given hour.
    :param hour: The hour in "HH:MM" format.
    :return: The appropriate greeting.
    """

    times = {
        "morning": (5, 11),
        "afternoon": (12, 17),
        "evening": (18, 21),
        "night": (22, 23),
        "night_": (0, 4),
    }

    for period, (start, end) in times.items():
        if start <= int(hour[:2]) <= end:
            period = period.replace("_", "")
            return f"Good {period}"


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["06:30"], "result": "Good morning"},
        {"parameters": ["12:00"], "result": "Good afternoon"},
        {"parameters": ["21:59"], "result": "Good evening"},
        {"parameters": ["00:01"], "result": "Good night"},
        {"parameters": ["11:30"], "result": "Good morning"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_greeting(test['parameters'][0])
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