# Daily challenge 2026-04-01: Prank Number
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-01
#
# Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.
# The pattern will be one of:
# 
# The numbers increase from one to the next by a fixed amount (addition).
# The numbers decrease from one to the next by a fixed amount (subtraction).
# 
# For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].

from typing import TypedDict


# Challenge
def fix_prank_number(arr: list) -> list:
    """
    Corrects a sequence that is expected to follow a constant step (arithmetic progression),
    where exactly one element is incorrect.

    :param arr: List of numbers forming an almost consistent pattern (one wrong value)
    :return: A corrected list where the pattern is consistent
    """

    # Count the frequency of differences between consecutive elements
    # This helps identify the intended common difference of the sequence
    variations = {}

    for i in range(len(arr) - 1):
        variation = arr[i + 1] - arr[i]
        variations[variation] = variations.get(variation, 0) + 1

    debug("variations", variations)

    # Determine the most common difference (assumed to be the correct one)
    max_variation = max(variations, key=variations.get)
    debug("most frequently variation", max_variation)

    # Attempt to fix the sequence by adjusting each position one at a time
    for i in range(len(arr)):
        # Work on a copy to avoid mutating the original input
        pattern = arr.copy()

        # Adjust one element to enforce the expected difference
        # Special handling when modifying the last index (wrap-around logic)
        if i == len(arr) - 1:
            pattern[0] = arr[1] - max_variation
        else:
            pattern[i + 1] = arr[i] + max_variation

        # Validate whether the modified sequence follows the expected pattern
        debug("try pattern", pattern)
        result = True

        for j in range(len(pattern) - 1):
            variation = pattern[j + 1] - pattern[j]
            if variation != max_variation:
                result = False

        # If all consecutive differences match, the sequence is corrected
        if result == True:
            return pattern

    return [0]

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[2, 4, 7, 8, 10]], "result": [2, 4, 6, 8, 10]},
        {"parameters": [[10, 10, 8, 7, 6]], "result": [10, 9, 8, 7, 6]},
        {"parameters": [[12, 24, 36, 48, 61, 72, 84, 96]], "result": [12, 24, 36, 48, 60, 72, 84, 96]},
        {"parameters": [[4, 1, -2, -5, -8, -5]], "result": [4, 1, -2, -5, -8, -11]},
        {"parameters": [[0, 100, 200, 300, 150, 500]], "result": [0, 100, 200, 300, 400, 500]},
        {"parameters": [[400, 425, 400, 375, 350, 325, 300]], "result": [450, 425, 400, 375, 350, 325, 300]},
        {"parameters": [[-5, 5, 10, 15, 20]], "result": [0, 5, 10, 15, 20]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = fix_prank_number(test['parameters'][0])
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