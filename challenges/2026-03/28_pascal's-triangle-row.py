# Daily challenge 2026-03-28: Pascal's Triangle Row
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-28
#
# Given an integer n, return the nth row of Pascal's triangle as an array.
# In Pascal's Triangle, each row begins and ends with 1, and each interior value is the sum of the two values directly above it.
# Here's the first 5 rows of the triangle:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# 

from typing import TypedDict


# Challenge
def pascal_row(n: int) -> list:
    """
    Return the n-th row (1-based) of Pascal's triangle.

    :param n: Row number (starting from 1)
    :return: List containing the values of the requested row
    """
    return get_pascal_triangle(n)[n - 1]


def get_pascal_triangle(num_rows):
    """
    Generate Pascal's triangle up to the given number of rows.

    :param num_rows: Total number of rows to generate
    :return: A list of rows, where each row is a list of integers
    """
    result = []
    i = -1

    while len(result) < num_rows:
        i += 1

        # Initialize the first and second rows directly
        if i == 0:
            result.append([1])
            continue
        elif i == 1:
            result.append([1, 1])
            continue

        # Retrieve the previous row to build the next one
        last_row = result[i - 1]

        # Start the new row with the leading 1
        new_row = [1]

        # Compute intermediate values by summing adjacent elements
        for n in range(len(last_row) - 1):
            new_row.append(last_row[n] + last_row[n + 1])

        # End the row with a trailing 1
        new_row.append(1)

        # Append the constructed row to the result
        result.append(new_row)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [5], "result": [1, 4, 6, 4, 1]},
        {"parameters": [3], "result": [1, 2, 1]},
        {"parameters": [1], "result": [1]},
        {"parameters": [10], "result": [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]},
        {"parameters": [15], "result": [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = pascal_row(test['parameters'][0])
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