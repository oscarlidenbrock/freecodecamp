# Daily challenge 2025-11-09: Word Search
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-09
#
# Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.
# 
# The given matrix will be filled with all lowercase letters (a-z).
# The word to find will always be in the matrix exactly once.
# The word to find will always be in a straight line in one of these directions:
# 
# left to right
# right to left
# top to bottom
# bottom to top
#
# For example, given the matrix:
# [
#   ["a", "c", "t"],
#   ["t", "a", "t"],
#   ["c", "t", "c"]
# ]
# 
# And the word "cat", return:
# [[0, 1], [2, 1]]
# 
# Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t" (end of the word).

from typing import TypedDict


# Challenge
def find_word(matrix: list, word: str) -> list:
    """
    Search for a word in a matrix.

    :param matrix: A list of lists representing the matrix.
    :param word: The word to search for.
    :return: Returns a list of lists containing the start and end indices of the word.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Allowed directions: right, left, down, and up.
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != word[0]:
                continue

            for row_step, col_step in directions:
                end_row = row + row_step * (len(word) - 1)
                end_col = col + col_step * (len(word) - 1)

                # Skip directions where the word would go outside the matrix.
                if end_row < 0 or end_row >= rows or end_col < 0 or end_col >= cols:
                    continue

                # Check every letter in the selected direction.
                for index in range(len(word)):
                    current_row = row + row_step * index
                    current_col = col + col_step * index

                    if matrix[current_row][current_col] != word[index]:
                        break
                else:
                    return [[row, col], [end_row, end_col]]


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat"], "result": [[0, 1], [2, 1]]},
        {"parameters": [[["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog"], "result": [[0, 0], [0, 2]]},
        {"parameters": [[["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish"], "result": [[3, 3], [0, 3]]},
        {"parameters": [[["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox"], "result": [[1, 3], [1, 1]]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = find_word(test['parameters'][0], test['parameters'][1])
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
