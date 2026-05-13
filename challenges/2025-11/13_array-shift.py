# Daily challenge 2025-11-13: Array Shift
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-13
#
# Given an array and an integer representing how many positions to shift the array, return the shifted array.
# 
# A positive integer shifts the array to the left.
# A negative integer shifts the array to the right.
# The shift wraps around the array.
# 
# For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].

from typing import TypedDict


# Challenge
def shift_array(arr: list, n: int) -> list:

    return arr

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[1, 2, 3], 1], "result": [2, 3, 1]},
        {"parameters": [[1, 2, 3], -1], "result": [3, 1, 2]},
        {"parameters": [["alpha", "bravo", "charlie"], 5], "result": ["charlie", "alpha", "bravo"]},
        {"parameters": [["alpha", "bravo", "charlie"], -11], "result": ["bravo", "charlie", "alpha"]},
        {"parameters": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15], "result": [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = shift_array(test['parameters'][0], test['parameters'][1])
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