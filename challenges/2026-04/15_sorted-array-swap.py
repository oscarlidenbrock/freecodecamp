# Daily challenge 2026-04-15: Sorted Array Swap
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-15
#
# Given an array of integers, return a new array using the following rules:
# 
# Sort the integers in ascending order
# Then swap all values whose index is a multiple of 3 with the value before it.
# 

from typing import TypedDict


# Challenge
def sort_and_swap(arr: list) -> list:
    """
    Sort the integers in ascending order and swap all values whose index is a multiple of 3 with the value before it.
    :param arr: The input array
    :return: A new array with the sorted and swapped values
    """

    # Sort the array in ascending order
    result = arr.copy()
    result.sort()

    # Swap all values whose index is a multiple of 3 with the value before it
    for i in range(1, len(result)):
        if i % 3 == 0:
            result[i], result[i-1] = result[i-1], result[i]

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[3, 1, 2, 4, 6, 5]], "result": [1, 2, 4, 3, 5, 6]},
        {"parameters": [[9, 7, 5, 3, 1, 2, 4, 6, 8]], "result": [1, 2, 4, 3, 5, 7, 6, 8, 9]},
        {"parameters": [[1, 2, 3, 4, 5, 6, 7, 8, 9]], "result": [1, 2, 4, 3, 5, 7, 6, 8, 9]},
        {"parameters": [[12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11]], "result": [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 11, 12]},
        {"parameters": [[100, -50, 0, 75, -25, 50, -75, 25]], "result": [-75, -50, 0, -25, 25, 75, 50, 100]},
        {"parameters": [[5, 9, 13, 77, 88, 313, -10, -65, 0, 8, 99, 101, -4, 2]], "result": [-65, -10, 0, -4, 2, 8, 5, 9, 77, 13, 88, 101, 99, 313]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = sort_and_swap(test['parameters'][0])
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
