# Daily challenge 2025-10-07: Space Week Day 4: Landing Spot
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-07
#
# In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:
# 
# Each spot in the matrix will contain a number from 0-9, inclusive.
# Any 0 represents a potential landing spot.
# Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
# The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
# Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
# Return the indices of the safest landing spot. There will always only be one safest spot.
# 
# For instance, given:
# [
#   [1, 0],
#   [2, 0]
# ]
# 
# Return [0, 1], the indices for the 0 in the first array.

from typing import TypedDict


# Challenge
def find_landing_spot(matrix: list) -> list:
    """
    Find the position with the lowest surrounding danger among the safest cells.

    :param matrix: An array of arrays representing the landing spots.
    :return: The row and column of the chosen landing spot.
    """

    # First, find the lowest cell value in the matrix.
    min_landing = 10

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] < min_landing:
                min_landing = matrix[y][x]

    debug("min_landing", min_landing)

    # Among cells with that minimum value, keep the one with the lowest
    # sum of orthogonal neighbors.
    min_danger = 99
    min_danger_pos = [-1, -1]

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] != min_landing: continue
            debug("checking position", [y, x])
            danger = 0

            if y > 0:
                danger += matrix[y - 1][x]
            if y < len(matrix) - 1:
                danger += matrix[y + 1][x]
            if x > 0:
                danger += matrix[y][x - 1]
            if x < len(matrix[y]) - 1:
                danger += matrix[y][x + 1]

            if danger < min_danger:
                min_danger = danger
                min_danger_pos = [y, x]

    return min_danger_pos



# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[[1, 0], [2, 0]]], "result": [0, 1]},
        {"parameters": [[[9, 0, 3], [7, 0, 4], [8, 0, 5]]], "result": [1, 1]},
        {"parameters": [[[1, 2, 1], [0, 0, 2], [3, 0, 0]]], "result": [2, 2]},
        {"parameters": [[[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]], "result": [2, 1]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = find_landing_spot(test['parameters'][0])
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
