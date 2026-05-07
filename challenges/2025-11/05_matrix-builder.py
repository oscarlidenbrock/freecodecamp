# Daily challenge 2025-11-05: Matrix Builder
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-05
#
# Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.
# For example, given 2 and 3, return:
# [
#   [0, 0, 0],
#   [0, 0, 0]
# ]
# 

from typing import TypedDict


# Challenge
def build_matrix(rows: int, cols: int) -> list[list[int]]:
    """
    Return a matrix filled with zeros (0) of the given size.

    :param rows: The number of rows in the matrix.
    :param cols: The number of columns in the matrix.
    :return: Returns a matrix filled with zeros (0) of the given size.
    """

    result = []

    for i in range(rows):
        row = [0] * cols
        result.append(row)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [2, 3], "result": [[0, 0, 0], [0, 0, 0]]},
        {"parameters": [3, 2], "result": [[0, 0], [0, 0], [0, 0]]},
        {"parameters": [4, 3], "result": [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]},
        {"parameters": [9, 1], "result": [[0], [0], [0], [0], [0], [0], [0], [0], [0]]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = build_matrix(test['parameters'][0], test['parameters'][1])
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