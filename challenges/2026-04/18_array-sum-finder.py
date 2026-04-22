# Daily challenge 2026-04-18: Array Sum Finder
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-18
#
# Given an array of numbers and a target number, return the first subset of two or more numbers that adds up to the target.
# 
# The "first" subset is the one whose elements have the lowest possible indices, prioritizing the earliest index first.
# Each number in the array may only be used once.
# If no valid subset exists, return "Sum not found".
# 
# Return the matching numbers as an array in the order they appear in the original array.

from typing import TypedDict


# Challenge
def find_sum(numbers: list, target: int) -> list | str:
    """
    Return the first subset whose values add up to ``target``.

    The search is performed recursively from left to right. At each position
    the function first tries including the current number and then skipping it,
    which preserves the challenge rule that prioritizes earlier indices.
    """

    def search(index: int, current: list, current_total: int) -> list:
        """
        Recursively build candidate subsets until every number has been
        considered.

        "index" tracks the next position to inspect, "current" stores the
        subset built so far, and "current_total" is the running sum for that
        subset.
        """

        # Base case: once every position has been considered, only return
        # subsets that meet both challenge conditions.
        if index == len(numbers):
            if len(current) >= 2 and current_total == target:
                return current.copy()
            return []

        # Try the branch that keeps the current value first so earlier indices
        # are prioritized in the first valid result.
        with_current = search(
            index + 1,
            current + [numbers[index]],
            current_total + numbers[index],
        )

        if with_current:
            return with_current

        # If including the current value does not work, continue without it.
        return search(index + 1, current, current_total)

    result = search(0, [], 0)
    return result if result else "Sum not found"


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[1, 3, 5, 7], 6], "result": [1, 5]},
        {"parameters": [[1, 2, 3, 4, 5], 5], "result": [1, 4]},
        {"parameters": [[1, 2, 3, 4, 5], 6], "result": [1, 2, 3]},
        {"parameters": [[-1, -2, 3, 4], 1], "result": [-1, -2, 4]},
        {"parameters": [[3, 1, 4, 1, 5, 9, 2, 6], 10], "result": [3, 1, 4, 2]},
        {"parameters": [[1, 2, 3, 4, 5, 6, 7, 8, 9], 20], "result": [1, 2, 3, 5, 9]},
        {"parameters": [[7, 9, 4, 2, 5], 10], "result": "Sum not found"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = find_sum(test['parameters'][0], test['parameters'][1])
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
