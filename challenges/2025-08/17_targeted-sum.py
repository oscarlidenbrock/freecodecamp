# Daily challenge 2025-08-17: Targeted Sum
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-17
#
# Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.
# 
# The returned array should have the indices in ascending order.
# 

from typing import TypedDict


# Challenge
def find_target(numbers: list, target: int) -> list | str:
    """
    Find two numbers in a list whose sum equals the target value.
    :param numbers: List of numbers
    :param target: Target value to find
    :return: A list with the positions of the two numbers whose sum equals the target value
    """

    # Iterate through each number in the list
    for i in range(len(numbers)):
        number = numbers[i]

        # Check the remaining numbers to see if their sum equals the target value
        for j in range(i + 1, len(numbers)):
            sum = numbers[i] + numbers[j]

            if sum == target:
                return [i, j]

    return "Target not found"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[2, 7, 11, 15], 9], "result": [0, 1]},
        {"parameters": [[3, 2, 4, 5], 6], "result": [1, 2]},
        {"parameters": [[1, 3, 5, 6, 7, 8], 15], "result": [4, 5]},
        {"parameters": [[1, 3, 5, 7], 14], "result": "Target not found"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = find_target(test['parameters'][0], test['parameters'][1])
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