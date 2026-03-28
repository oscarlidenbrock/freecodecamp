# Daily challenge 2025-09-12: Screen Time
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-12
#
# Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:
# 
# If any single day has 10 hours or more, it's too much.
# If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
# If the average of the seven days is greater than or equal to 6 hours, it's too much.
# 

from typing import TypedDict


# Challenge
def too_much_screen_time(hours: list) -> bool:
    """
    Determine whether screen time usage is excessive over a week.

    :param hours: List of 7 values representing daily screen time (in hours)
    :return: True if usage is considered excessive, otherwise False
    """

    # Sort the list in ascending order to easily access highest values
    hours.sort()

    # Check if any single day has 10 or more hours of usage
    if hours[-1] >= 10:
        return True

    # Check if the average of the top 3 highest-usage days is at least 8 hours
    if sum(hours[-3:]) / 3 >= 8:
        return True

    # Check if the overall weekly average is at least 6 hours per day
    if sum(hours) / 7 >= 6:
        return True

    # If none of the conditions are met, usage is not excessive
    return False

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": [[1, 2, 3, 4, 5, 6, 7]], "result": False},
        {"parameters": [[7, 8, 8, 4, 2, 2, 3]], "result": False},
        {"parameters": [[5, 6, 6, 6, 6, 6, 6]], "result": False},
        {"parameters": [[1, 2, 3, 11, 1, 3, 4]], "result": True},
        {"parameters": [[1, 2, 3, 10, 2, 1, 0]], "result": True},
        {"parameters": [[3, 3, 5, 8, 8, 9, 4]], "result": True},
        {"parameters": [[3, 9, 4, 8, 5, 7, 6]], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = too_much_screen_time(test['parameters'][0])
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