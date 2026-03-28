# Daily challenge 2025-09-13: Missing Numbers
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-13
#
# Given an array of integers from 1 to n, inclusive, return an array of all the missing integers between 1 and n (where n is the largest number in the given array).
# 
# The given array may be unsorted and may contain duplicates.
# The returned array should be in ascending order.
# If no integers are missing, return an empty array.
# 

from typing import TypedDict


# Challenge
def find_missing_numbers(arr: list) -> list:
    """
    Return all missing integers within the range defined by the
    minimum and maximum values in the input list.

    :param arr: List of integers
    :return: List of missing integers within the range [min(arr), max(arr)]
    """

    # Determine the lower and upper bounds of the range
    lower_num = min(arr)
    upper_num = max(arr)
    result = []

    # Iterate through the full range and collect numbers not present in the list
    for i in range(lower_num, upper_num + 1):
        if i not in arr:
            result.append(i)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[1, 3, 5]], "result": [2, 4]},
        {"parameters": [[1, 2, 3, 4, 5]], "result": []},
        {"parameters": [[1, 10]], "result": [2, 3, 4, 5, 6, 7, 8, 9]},
        {"parameters": [[10, 1, 10, 1, 10, 1]], "result": [2, 3, 4, 5, 6, 7, 8, 9]},
        {"parameters": [[3, 1, 4, 1, 5, 9]], "result": [2, 6, 7, 8]},
        {"parameters": [[1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]], "result": [11]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = find_missing_numbers(test['parameters'][0])
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