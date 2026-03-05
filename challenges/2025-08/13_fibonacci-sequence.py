# Daily challenge 2025-08-13: Fibonacci Sequence
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-13
#
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with 0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
# Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.
# 
# Your function should handle sequences of any length greater than or equal to zero.
# If the length is zero, return an empty array.
# Note that the starting numbers are part of the sequence.
# 

from typing import TypedDict


# Challenge
def fibonacci_sequence(start_sequence: list, length: int) -> list:
    """
    Return a Fibonacci sequence starting from two initial numbers.

    :param start_sequence: A list containing the first two numbers of the sequence.
    :param length: The length of the resulting Fibonacci sequence.
    :return: The generated Fibonacci sequence.
    """
    result = []

    # If length is 0, return an empty list
    if length == 0:
        return result

    # Add the first number of the starting sequence
    result.append(start_sequence[0])

    if length == 1:
        # If only one element is required, return the list with the first value
        return result
    else:
        # Otherwise, add the second number of the starting sequence
        result.append(start_sequence[1])

    # Complete the Fibonacci sequence
    while len(result) < length:
        result.append(result[-2] + result[-1])

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[0, 1], 20], "result": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]},
        {"parameters": [[21, 32], 1], "result": [21]},
        {"parameters": [[0, 1], 0], "result": []},
        {"parameters": [[10, 20], 2], "result": [10, 20]},
        {"parameters": [[123456789, 987654321], 5], "result": [123456789, 987654321, 1111111110, 2098765431, 3209876541]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if fibonacci_sequence(test['parameters'][0], test['parameters'][1]) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")

test()