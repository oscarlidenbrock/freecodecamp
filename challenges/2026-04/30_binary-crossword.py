# Daily challenge 2026-04-30: Binary Crossword
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-30
#
# Given a character, determine if its 8-bit binary representation can be found in the following grid, horizontally or vertically in either direction:
# 0 1 0 0 0 0 0 1
# 0 1 1 0 1 1 1 1
# 0 1 0 0 0 1 0 0
# 0 1 1 0 0 1 0 1
# 0 1 0 1 0 0 1 0
# 0 1 0 1 0 1 0 0
# 0 1 1 0 1 0 0 0
# 1 0 1 0 1 1 1 0
# 
# For example, "A" has the binary representation 01000001, which appears in the first row from left to right.

from typing import TypedDict


# Challenge
def is_in_crossword(char: str) -> bool:
    """
    Check whether the character's 8-bit binary value appears in the grid.

    The binary value may appear horizontally or vertically, in either the
    normal or reversed direction.

    :param char: The character whose binary representation will be searched.
    :return: True if the 8-bit binary representation is found, False otherwise.
    """

    crossword_grid = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0]
    ]

    # Convert the character to its 8-bit binary string, for example "A" -> "01000001".
    char_binary = format(ord(char), '08b')
    debug("char_binary", char_binary)

    # Check each row from left to right and from right to left.
    for row in crossword_grid:
        row_str = ''.join(map(str, row))

        if row_str == char_binary or row_str == char_binary[::-1]:
            return True

    # Build each column as a string, then check top to bottom and bottom to top.
    for i in range(len(crossword_grid)):
        row_str = ""

        for j in range(len(crossword_grid[i])):
            row_str += str(crossword_grid[j][i])

        if row_str == char_binary or row_str == char_binary[::-1]:
            return True

    return False

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["I"], "result": True},
        {"parameters": ["D"], "result": True},
        {"parameters": ["0"], "result": True},
        {"parameters": ["u"], "result": True},
        {"parameters": ["Y"], "result": False},
        {"parameters": ["p"], "result": False},
        {"parameters": ["1"], "result": False},
        {"parameters": ["Q"], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_in_crossword(test['parameters'][0])
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
