# Daily challenge 2026-03-09: Array Sum
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-09
#
# Given an array of numbers, return the sum of all the numbers.

from typing import TypedDict


# Challenge
def sum_array(numbers: list) -> int:
    """
    Return the sum of all values in the list.

    :param numbers: List of numeric values.
    :return: Sum of the list elements.
    """
    return sum(numbers)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [[1, 2, 3, 4, 5]], "result": 15},
        {"parameters": [[42]], "result": 42},
        {"parameters": [[5, -2, 7, -3]], "result": 7},
        {"parameters": [[203, 145, -129, 6293, 523, -919, 845, 2434]], "result": 9395},
        {"parameters": [[0, 0]], "result": 0},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = sum_array(test['parameters'][0])
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