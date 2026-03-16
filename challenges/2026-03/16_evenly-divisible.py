# Daily challenge 2026-03-16: Evenly Divisible
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-16
#
# Given two integers, determine if you can evenly divide the first one by the second one.

from typing import TypedDict


# Challenge
def is_evenly_divisible(a: int, b: int) -> bool:
    """
    Determine whether integer "a" is evenly divisible by integer "b".

    :param a: The number to be divided
    :param b: The divisor
    :return: True if "a" is divisible by "b" without a remainder, otherwise False
    """

    # The modulo operator (%) returns the remainder of the division.
    # If the remainder is 0, the division is exact.
    return a % b == 0

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": [4, 2], "result": True},
        {"parameters": [7, 3], "result": False},
        {"parameters": [5, 10], "result": False},
        {"parameters": [48, 6], "result": True},
        {"parameters": [3186, 9], "result": True},
        {"parameters": [4192, 11], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_evenly_divisible(test['parameters'][0], test['parameters'][1])
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