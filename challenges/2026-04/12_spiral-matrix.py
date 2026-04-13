# Daily challenge 2026-04-12: Spiral Matrix
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-12
#
# Given a 2D matrix, return a flat array with all of its values in clockwise order.
# The returned array should have the top-left value first, move right along the top row, then down the right column, then left along the bottom row, then up the left column. Repeat inward for any remaining layers.
# For example, given:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# 
# Return [1, 2, 3, 6, 9, 8, 7, 4, 5].

from typing import TypedDict


# Challenge
def spiral_matrix(matrix: list) -> list:
    """
    Traverse a 2D matrix in clockwise spiral order.
    This process repeats until all elements are consumed.

    :param matrix: 2D list representing the matrix
    :return: List of elements in clockwise spiral order
    """

    # Work on a shallow copy to avoid mutating the original input
    matrix_c = matrix.copy()

    result = []

    # Direction state machine controlling traversal order
    direction = "left-right"

    # Loop until all elements have been removed from the matrix copy
    end = False

    while not end:
        # Extract elements based on current traversal direction
        match direction:

            case "left-right":
                # Traverse the top row from left to right
                for i in range(len(matrix_c[0])):
                    result.append(matrix_c[0][i])

                # Remove the consumed top row
                del matrix_c[0]

                # Next direction: right column, top → bottom
                direction = "right-down"

            case "right-down":
                # Traverse the rightmost column from top to bottom
                for i in range(len(matrix_c)):
                    result.append(matrix_c[i][-1])

                    # Remove the consumed element from each row
                    del matrix_c[i][-1]

                # Next direction: bottom row, right → left
                direction = "down-left"

            case "down-left":
                # Traverse the bottom row from right to left
                for i in range(len(matrix_c[-1]) - 1, -1, -1):
                    result.append(matrix_c[-1][i])

                # Remove the consumed bottom row
                del matrix_c[-1]

                # Next direction: left column, bottom → top
                direction = "left-up"

            case "left-up":
                # Traverse the leftmost column from bottom to top
                for i in range(len(matrix_c) - 1, -1, -1):
                    result.append(matrix_c[i][0])

                    # Remove the consumed element from each row
                    del matrix_c[i][0]

                # Reset cycle to top row traversal
                direction = "left-right"

        # if all rows are empty, traversal is complete
        remaining_elements = sum(len(row) for row in matrix_c)
        if remaining_elements == 0:
            end = True

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "result": [1, 2, 3, 6, 9, 8, 7, 4, 5]},
        {"parameters": [[["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]]], "result": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]},
        {"parameters": [[[True, False, False], [False, True, True], [False, True, False], [True, True, False]]], "result": [True, False, False, True, False, False, True, True, False, False, True, True]},
        {"parameters": [[[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]]], "result": [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = spiral_matrix(test['parameters'][0])
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