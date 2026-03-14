# Daily challenge 2026-03-14: Pi Day
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-14
#
# Happy pi (π) day!
# Given an integer (n), where n is between 1 and 1000 (inclusive), return the nth decimal of π.
# 
# Make sure to return a number not a string.
# 
# π with its first five decimals is 3.14159. So given 5 for example, return 9, the fifth decimal.
# You may have to find the first 1000 decimals of π somewhere.
#

from typing import TypedDict
from decimal import Decimal, getcontext

# Challenge
def get_pi_decimal(pos: int) -> int:
    """
    Returns the nth decimal digit of pi.

    :param pos: Position of the decimal digit (1-based)
    :return: An integer representing the nth decimal digit of pi
    """
    # Get pi as a string
    pi = get_pi_number(pos)

    # Return the decimal digit at the specified position
    return int(str(pi).split('.')[1][pos - 1])


def get_pi_number(decimals) -> str:
    """
    Calculates pi to a specified number of decimal places using the Chudnovsky series.

    :param decimals: Number of decimal digits to calculate
    :return: A string representation of pi with the requested number of decimals
    """

    # Set the precision slightly higher to avoid rounding errors
    getcontext().prec = decimals + 10

    # Chudnovsky series constants
    C = 426880 * Decimal(10005).sqrt()
    M = Decimal(1)
    L = Decimal(13591409)
    X = Decimal(1)
    K = Decimal(6)
    S = L

    # Number of terms needed (~14 digits per term)
    n_terms = (decimals // 14) + 1

    for i in range(1, n_terms):
        M = M * (K ** 3 - 16 * K) / (i ** 3)
        L += 545140134
        X *= -262537412640768000
        S += M * L / X
        K += 12

    pi = C / S

    # Convert to string and keep only the requested number of decimals ("3." + decimals)
    result = str(pi)[:decimals + 2]

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [5], "result": 9},
        {"parameters": [10], "result": 5},
        {"parameters": [22], "result": 6},
        {"parameters": [39], "result": 7},
        {"parameters": [76], "result": 2},
        {"parameters": [384], "result": 4},
        {"parameters": [601], "result": 0},
        {"parameters": [1000], "result": 9},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_pi_decimal(test['parameters'][0])
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