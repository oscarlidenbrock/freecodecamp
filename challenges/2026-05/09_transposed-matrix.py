# Daily challenge 2026-05-09: Transposed Matrix
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-09
#
# Given a matrix (an array of arrays), return the transposed version of it.
# To transpose the matrix, swap the rows and columns. E.g: a value at index [0, 1] should move to index [1, 0].
# For example, given:
# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
# 
# Return:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]
# 

from typing import TypedDict


# Challenge
def transpose(matrix: list) -> list:
    """
    Get the transposed version of a matrix.

    :param matrix: A list of lists representing a matrix.
    :return: Returns the transposed version of the matrix.
    """

    result = []

    for i in range(len(matrix[0])):
        result.append([])

        for j in range(len(matrix)):
            result[i].append(matrix[j][i])

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[[1, 2, 3], [4, 5, 6]]], "result": [[1, 4], [2, 5], [3, 6]]},
        {"parameters": [[[1, 2], [3, 4], [5, 6]]], "result": [[1, 3, 5], [2, 4, 6]]},
        {"parameters": [[[1, 2], [3, 4], [5, 6], [7, 8]]], "result": [[1, 3, 5, 7], [2, 4, 6, 8]]},
        {"parameters": [[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]]], "result": [["a", "d", "g", "j"], ["b", "e", "h", "k"], ["c", "f", "i", "l"]]},
        {"parameters": [[[True, False, True, False], [False, True, False, True], [True, True, False, False], [False, False, True, True], [True, False, False, True]]], "result": [[True, False, True, False, True], [False, True, True, False, False], [True, False, False, True, False], [False, True, False, True, True]]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = transpose(test['parameters'][0])
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