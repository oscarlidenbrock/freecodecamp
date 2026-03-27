# Daily challenge 2025-09-10: Array Diff
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-10
#
# Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.
# 
# The returned array should be sorted in alphabetical order.
# 

from typing import TypedDict


# Challenge
def array_diff(arr1: list, arr2: list) -> list:
    """
    Return the symmetric difference between two lists.

    The result contains elements that appear in either list,
    but not in both. The final list is sorted before returning.

    :param arr1: First input list.
    :param arr2: Second input list.
    :return: A sorted list of elements unique to each list.
    """
    result = []

    # Add elements that are in arr2 but not in arr1
    for item in arr2:
        if item not in arr1:
            result.append(item)

    # Add elements that are in arr1 but not in arr2
    for item in arr1:
        if item not in arr2:
            result.append(item)

    # Sort the result list before returning
    result.sort()

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [["apple", "banana"], ["apple", "banana", "cherry"]], "result": ["cherry"]},
        {"parameters": [["apple", "banana", "cherry"], ["apple", "banana"]], "result": ["cherry"]},
        {"parameters": [["one", "two", "three", "four", "six"], ["one", "three", "eight"]], "result": ["eight", "four", "six", "two"]},
        {"parameters": [["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]], "result": ["five", "one", "seven", "three"]},
        {"parameters": [["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]], "result": ["freeCodeCamp", "rocks"]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = array_diff(test['parameters'][0], test['parameters'][1])
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