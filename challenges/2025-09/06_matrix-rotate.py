# Daily challenge 2025-09-06: Matrix Rotate
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-06
#
# Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it. For instance, given [[1, 2], [3, 4]], which looks like this:
# 
# 1, 2
# 3, 4
#
# You should return [[3, 1], [4, 2]], which looks like this:
#
# 3, 1
# 4, 2
#

from typing import TypedDict


# Challenge
def rotate(matrix: list) -> list:
    """
    Rotates a 2D matrix 90 degrees clockwise.

    :param matrix: List of lists representing the matrix.
    :return: New matrix rotated 90° clockwise.
    """

    return [list(row) for row in zip(*matrix[::-1])]

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[[1]]], "result": [[1]]},
        {"parameters": [[[1, 2], [3, 4]]], "result": [[3, 1], [4, 2]]},
        {"parameters": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "result": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]},
        {"parameters": [[[0, 1, 0], [1, 0, 1], [0, 0, 0]]], "result": [[0, 1, 0], [0, 0, 1], [0, 1, 0]]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = rotate(test['parameters'][0])
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