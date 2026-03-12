# Daily challenge 2025-08-20: 3 Strikes
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-20
#
# Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3.

from typing import TypedDict


# Challenge
def squares_with_three(n: int) -> int:
    """
    Given an integer up to 10,000, return how many numbers from 1 to n
    have a square that contains the digit 3.

    :param n: the upper limit of the range
    :return: the count of squares containing the digit 3
    """

    result = 0

    for i in range(1, n):
        if "3" in str(i ** 2):
            result += 1

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [1], "result": 0},
        {"parameters": [10], "result": 1},
        {"parameters": [100], "result": 19},
        {"parameters": [1000], "result": 326},
        {"parameters": [10000], "result": 4531},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = squares_with_three(test['parameters'][0])
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