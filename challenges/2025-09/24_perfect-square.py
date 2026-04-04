# Daily challenge 2025-09-24: Perfect Square
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-24
#
# Given an integer, determine if it is a perfect square.
# 
# A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.
# 

from typing import TypedDict

# Challenge
def is_perfect_square(n):
    """
    Determine whether a number is a perfect square.

    A perfect square is a number whose square root is an integer.
    The function handles both real and complex inputs: any number
    resulting in a complex square root is not considered a perfect square.

    :param n: The number to evaluate (can be int or float)
    :return: True if n is a perfect square, False otherwise
    """

    # Calculate the square root of the number
    square = n ** 0.5

    # If the result is complex, n cannot be a perfect square in the reals
    if isinstance(square, complex):
        return False

    # Check if the square root is an integer
    return square.is_integer()

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": [9], "result": True},
        {"parameters": [49], "result": True},
        {"parameters": [1], "result": True},
        {"parameters": [2], "result": False},
        {"parameters": [99], "result": False},
        {"parameters": [-9], "result": False},
        {"parameters": [0], "result": True},
        {"parameters": [25281], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_perfect_square(test['parameters'][0])
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