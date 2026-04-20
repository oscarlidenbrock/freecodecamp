# Daily challenge 2026-04-19: Unique Stair Climber
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-19
#
# Given a number of stairs, return how many distinct ways someone can climb them taking either 1 or 2 steps at a time.

from typing import TypedDict


# Challenge
def get_unique_climbs(steps: int) -> int:
    """
    Given a number of stairs, return how many distinct ways someone can climb them taking either 1 or 2 steps at a time.

    :param steps: The number of stairs.
    :return: The number of distinct ways someone can climb the stairs.
    """
    if steps <= 1:
        return 1

    previous = 1
    current = 1

    for i in range(2, steps + 1):
        previous, current = current, previous + current

    return current

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [4], "result": 5},
        {"parameters": [5], "result": 8},
        {"parameters": [10], "result": 89},
        {"parameters": [18], "result": 4181},
        {"parameters": [29], "result": 832040},
        {"parameters": [50], "result": 20365011074},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_unique_climbs(test['parameters'][0])
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
