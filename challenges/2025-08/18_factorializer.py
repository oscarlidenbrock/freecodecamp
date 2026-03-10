# Daily challenge 2025-08-18: Factorializer
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-18
#
# Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.
# 
# The factorial of zero is 1.
# 

from typing import TypedDict


# Challenge
def factorial(number: int) -> int:
    """
    Calculate the factorial of a number.
    :param number: The given number
    :return: The factorial of the given number
    """
    result = 1

    # Calculate the factorial
    for n in range(1, number + 1):
        result = result * n

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [0], "result": 1},
        {"parameters": [5], "result": 120},
        {"parameters": [20], "result": 2432902008176640000},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = factorial(test['parameters'][0])
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