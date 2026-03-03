# Daily challenge 2026-02-27: Matrix Shift
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-27
#
# Given a matrix (array of arrays) of numbers and an integer, shift all values in the matrix by the given amount.
# 
# A positive shift moves values to the right.
# A negative shift moves values to the left.
# 
# Values should wrap:
# 
# Treat the matrix as one continuous sequence of values.
# When a value moves past the end of a row, it continues at the beginning of the next row.
# When a value moves past the last position in the matrix, it wraps to the first position.
# The same applies in reverse when shifting left.
# 
# For example, given:
# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
# 
# with a shift of 1, move all the numbers to the right one:
# [
#   [6, 1, 2],
#   [3, 4, 5]
# ]
# 

from typing import TypedDict


# Challenge
def shift_matrix(matrix, shift):

    return matrix

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [).assertEqual(shift_matrix([[1, 2, 3], [4, 5, 6]], 1], "result": [[6, 1, 2], [3, 4, 5]])`},
        {"parameters": [).assertEqual(shift_matrix([[1, 2, 3], [4, 5, 6]], -1], "result": [[2, 3, 4], [5, 6, 1]])`},
        {"parameters": [).assertEqual(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5], "result": [[5, 6, 7], [8, 9, 1], [2, 3, 4]])`},
        {"parameters": [).assertEqual(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6], "result": [[7, 8, 9], [1, 2, 3], [4, 5, 6]])`},
        {"parameters": [).assertEqual(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7], "result": [[10, 11, 12, 13], [14, 15, 16, 1], [2, 3, 4, 5], [6, 7, 8, 9]])`},
        {"parameters": [).assertEqual(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54], "result": [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]])`},
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if shift_matrix(test['parameters'][0], test['parameters'][1]) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")

test()