# Daily challenge 2026-05-13: Offending Element
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-13
#
# Given an array of integers that is sorted in ascending order except for one out-of-place element, return the index of that element.
# 
# If more than one element could be considered out of place, return the index of the first one.
# 

from typing import TypedDict


# Challenge
def find_offender(arr: list) -> int:
    """
    Return the index of the out-of-place element.

    :param arr: A sorted array of integers
    :return: The index of the out-of-place element
    """

    def is_sorted_without(index: int) -> bool:
        """
        Check if the array is sorted without the element at the given index.

        :param index: The index of the element to check
        :return: Returns True if the array is sorted without the element at the given index, False otherwise.
        """
        previous = None

        # Iterate through the array
        for n, value in enumerate(arr):
            # Skip the current element
            if n == index:
                continue

            # If the current element is less than the previous element, return False
            if previous is not None and value < previous:
                return False

            # Update the previous element
            previous = value

        # If we reach the end of the array without returning False, the array is sorted
        return True

    # Iterate through the array
    for n in range(len(arr)):
        # If the array is sorted without the current element, return it
        if is_sorted_without(n):
            return n

    # If we reach the end of the array without returning True, the array is not sorted
    return 0

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [[1, 6, 2, 3, 4, 5]], "result": 1},
        {"parameters": [[1, 2, 3, 5, 4, 5]], "result": 3},
        {"parameters": [[2, 1]], "result": 0},
        {"parameters": [[2, 4, 1, 6, 8]], "result": 2},
        {"parameters": [[5, 18, 24, 33, 40, 55, 15, 68, 84, 91]], "result": 6},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = find_offender(test['parameters'][0])
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
