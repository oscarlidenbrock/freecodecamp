# Daily challenge 2026-05-05: Narcissistic Number
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-05
#
# Given a positive integer, determine whether it is a narcissistic number.
# 
# A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
# 
# For example, 153 has 3 digits, and 13 + 53 + 33 = 153, so it is narcissistic.

from typing import TypedDict


# Challenge
def is_narcissistic(number: int) -> bool:
    """
    Determine whether a number is a narcissistic number.

    :param number: The number to evaluate.
    :return: Returns True if the number is a narcissistic number, False otherwise.
    """

    exp = len(str(number))
    sum = 0

    for digit in str(number):
        sum += int(digit) ** exp

    return sum == number

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": [153], "result": True},
        {"parameters": [154], "result": False},
        {"parameters": [371], "result": True},
        {"parameters": [512], "result": False},
        {"parameters": [9], "result": True},
        {"parameters": [11], "result": False},
        {"parameters": [9474], "result": True},
        {"parameters": [6549], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_narcissistic(test['parameters'][0])
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