# Daily challenge 2025-08-30: Array Duplicates
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-30
#
# Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in ascending order. If no values appear more than once, return an empty array.
# 
# Only include one instance of each value in the returned array.
# 

from typing import TypedDict


# Challenge
def find_duplicates(arr: list) -> list:
    """
    Return a sorted list of elements that appear more than once in the input list.

    :param arr: List of elements to analyze
    :return: Sorted list of duplicated elements (no repetitions in the result)
    """

    result = []

    # Iterate through each element in the input list
    for item in arr:
        # Check if the element appears more than once
        # and ensure it is added only once to the result
        if arr.count(item) > 1 and item not in result:
            result.append(item)

    # Sort the resulting list of duplicates
    result.sort()

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[1, 2, 3, 4, 5]], "result": []},
        {"parameters": [[1, 2, 3, 4, 1, 2]], "result": [1, 2]},
        {"parameters": [[2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]], "result": [-6, 0, 2, 4, 5, 23]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = find_duplicates(test['parameters'][0])
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