# Daily challenge 2026-03-19: Inverted Matrix
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-19
#
# Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.
# For example, given:
# [
#   ["a", "b"],
#   ["a", "a"]
# ]
# 
# Return:
# [
#   ["b", "a"],
#   ["b", "b"]
# ]
# 

from typing import TypedDict


# Challenge
def invert_matrix(matrix: list) -> list:
    """
    Swap the values in a 2D matrix containing exactly two distinct elements.

    Each occurrence of one value is replaced by the other, effectively
    inverting the matrix.

    :param matrix: A 2D list (list of lists) with exactly two unique values
    :return: The modified matrix with values swapped
    """
    result = []

    # Collect the unique values present in the matrix
    values = []
    for row in matrix:
        for item in row:
            if item not in values:
                values.append(item)

    debug("possible values:", values)

    # Replace each value with its counterpart across the matrix
    for row_index in range(len(matrix)):
        row = matrix[row_index]

        for col_index in range(len(row)):
            item = row[col_index]

            if item == values[0]:
                row[col_index] = values[1]
            else:
                row[col_index] = values[0]

        # Update the modified row back into the matrix
        matrix[row_index] = row

    return matrix

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[["a", "b"], ["a", "a"]]], "result": [["b", "a"], ["b", "b"]]},
        {"parameters": [[[1, 0, 1], [1, 1, 1], [0, 1, 0]]], "result": [[0, 1, 0], [0, 0, 0], [1, 0, 1]]},
        {"parameters": [[["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]]], "result": [["banana", "apple", "apple", "banana"], ["apple", "banana", "banana", "apple"], ["apple", "apple", "apple", "banana"]]},
        {"parameters": [[[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]]], "result": [[7, 6, 6, 6, 7], [6, 7, 6, 7, 6], [6, 6, 7, 6, 6], [6, 7, 6, 7, 6], [7, 6, 6, 6, 7]]},
        {"parameters": [[[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]], "result": [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = invert_matrix(test['parameters'][0])
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