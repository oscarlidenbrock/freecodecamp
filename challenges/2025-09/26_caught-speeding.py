# Daily challenge 2025-09-26: Caught Speeding
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-26
#
# Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.
# 
# If there were no vehicles speeding, return [0, 0].
# 

from typing import TypedDict


# Challenge
def speeding(speeds: list, limit: int) -> list:
    """
    Compute speeding statistics for a set of vehicle speeds.

    :param speeds: List of recorded vehicle speeds
    :param limit: Speed limit threshold
    :return: A list [count, avg_excess] where:
             - count: number of vehicles exceeding the limit
             - avg_excess: average amount by which those vehicles exceeded the limit
                           (0 if no vehicles were speeding)
    """

    # result[0] → count of speeding vehicles
    # result[1] → average excess speed over the limit
    result = [0, 0]

    # Stores how much each speeding vehicle exceeded the limit
    excess_speeds = []

    for speed in speeds:
        # Identify speeds strictly above the limit
        if speed > limit:
            result[0] += 1

            # Record the excess over the limit for later averaging
            excess_speeds.append(speed - limit)

    # Compute average excess only if there are speeding vehicles
    if len(excess_speeds) > 0:
        result[1] = sum(excess_speeds) / len(excess_speeds)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[50, 60, 55], 60], "result": [0, 0]},
        {"parameters": [[58, 50, 60, 55], 55], "result": [2, 4]},
        {"parameters": [[61, 81, 74, 88, 65, 71, 68], 70], "result": [4, 8.5]},
        {"parameters": [[100, 105, 95, 102], 100], "result": [2, 3.5]},
        {"parameters": [[40, 45, 44, 50, 112, 39], 55], "result": [1, 57]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = speeding(test['parameters'][0], test['parameters'][1])
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