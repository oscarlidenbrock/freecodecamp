# Daily challenge 2026-03-03: Perfect Cube Count
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-03
#
# Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.
# 
# The lower number is not garanteed to be the first argument.
# A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27.
# 

from typing import TypedDict


# Challenge
def count_perfect_cubes(num1: int, num2: int) -> int:
    """
    Return the perfect cubes between two numbers

    :param num1: First number
    :param num2: Second number
    :return: The perfect cube count
    """

    result = 0

    # Set the min and max numbers with the parameters
    min = num1
    max = num2

    if num1 > num2:
        min = num2
        max = num1

    if min > 1: min = 2

    # Get the perfect cubes in range
    for num in range(min, max + 1):
        cube_value = num ** 3

        if cube_value >= min and cube_value <= max:
            result += 1


    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [3, 30], "result": 2},
        {"parameters": [1, 30], "result": 3},
        {"parameters": [30, 0], "result": 4},
        {"parameters": [-64, 64], "result": 9},
        {"parameters": [9214, -8127], "result": 41},
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if count_perfect_cubes(test['parameters'][0], test['parameters'][1]) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")

test()