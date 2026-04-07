# Daily challenge 2025-09-25: 2nd Largest
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-25
#
# Given an array, return the second largest distinct number.

from typing import TypedDict


# Challenge
def second_largest(numbers: list) -> int:
    """
    Return the second largest distinct number in the list.

    :param numbers: List of numeric values
    :return: Second largest distinct number
    """

    # Remove duplicate values to ensure distinct comparison
    numbers = list(set(numbers))

    # Sort the list in ascending order
    numbers.sort()

    # Return the second largest element (penultimate in sorted list)
    return numbers[-2]

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [[1, 2, 3, 4]], "result": 3},
        {"parameters": [[20, 139, 94, 67, 31]], "result": 94},
        {"parameters": [[2, 3, 4, 6, 6]], "result": 4},
        {"parameters": [[10, -17, 55.5, 44, 91, 0]], "result": 55.5},
        {"parameters": [[1, 0, -1, 0, 1, 0, -1, 1, 0]], "result": 0},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = second_largest(test['parameters'][0])
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