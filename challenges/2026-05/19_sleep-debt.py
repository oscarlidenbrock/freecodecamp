# Daily challenge 2026-05-19: Sleep Debt
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-19
#
# Given an array of hours slept each night leading up to today, and a target number of hours per night, return how many hours of sleep you need tonight to eliminate your sleep debt.
# 
# Include tonight's hours in the total time needed to catch up.
# If you've slept enough to cover tonight's target or more, return 0.
# 

from typing import TypedDict


# Challenge
def sleep_debt(hours_slept: list, target_hours: int) -> int:
    """
    Get the sleep debt.

    :param hours_slept: A list of hours slept each night leading up to today.
    :param target_hours: The target number of hours per night.
    :return: Returns the sleep debt.
    """

    total_slept = sum(hours_slept)
    total_needed = target_hours * (len(hours_slept) + 1)

    return max(total_needed - total_slept, 0)


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [[6, 6, 6, 6, 6, 6], 8], "result": 20},
        {"parameters": [[6, 7, 8, 4, 8, 6], 7], "result": 10},
        {"parameters": [[10, 10, 9, 10, 9, 11], 9], "result": 4},
        {"parameters": [[8, 7, 6, 7, 6, 8], 6], "result": 0},
        {"parameters": [[8, 9, 10, 9, 10, 7], 7], "result": 0},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = sleep_debt(test['parameters'][0], test['parameters'][1])
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