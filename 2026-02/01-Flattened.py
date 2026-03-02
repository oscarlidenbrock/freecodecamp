# Daily challenge 01/02/2026: Flattened
#
# Given an array, determine if it is flat.
#
# An array is flat if none of its elements are arrays.

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
        value: list
        result: bool

    unitTest: list[UnitTest] = [
        {"value": [1, 2, 3, 4], "result": True},
        {"value": [1, [2, 3], 4], "result": False},
        {"value": [1, 0, False, True, "a", "b"], "result": True},
        {"value": ["a", [0], "b", True], "result": False},
        {"value": [1, [2, [3, [4, [5]]]], 6], "result": False}
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if is_flat(test['value']) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")


test()
