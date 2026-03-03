# Daily challenge 2026-03-01: Flattened
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-01
#
# Given an array, determine if it is flat.
# 
# An array is flat if none of its elements are arrays.
# 

from typing import TypedDict


# Challenge
def is_flat(input: list) -> bool:
    for element in input:
        if isinstance(element, list):
            return False

    return True

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": [[1, 2, 3, 4]], "result": True},
        {"parameters": [[1, [2, 3], 4]], "result": False},
        {"parameters": [[1, 0, False, True, "a", "b"]], "result": True},
        {"parameters": [["a", [0], "b", True]], "result": False},
        {"parameters": [[1, [2, [3, [4, [5]]]], 6]], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if is_flat(test['parameters'][0]) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")

test()