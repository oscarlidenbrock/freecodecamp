# Daily challenge 2025-08-19: Sum of Squares
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-19
#
# Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.

from typing import TypedDict


# Challenge
def sum_of_squares(n: int) -> int:
    """
    Calculate the sum of the squares of numbers from 1 to n.

    :param n: the upper limit of the range
    :return: the sum of the squares in the range
    """
    result = 0

    for i in range(1, n + 1):
        result += i ** 2

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [5], "result": 55},
        {"parameters": [10], "result": 385},
        {"parameters": [25], "result": 5525},
        {"parameters": [500], "result": 41791750},
        {"parameters": [1000], "result": 333833500},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = sum_of_squares(test['parameters'][0])
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