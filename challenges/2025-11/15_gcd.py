# Daily challenge 2025-11-15: GCD
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-15
#
# Given two positive integers, return their greatest common divisor (GCD).
# 
# The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.
# 
# For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6. So given 4 and 6, return 2, the largest number that appears in both sets of divisors.

from typing import TypedDict


# Challenge
def gcd(x: int, y: int ) -> int:
    """
    Gives the greatest common divisor of two integers.

    :param x: The first integer.
    :param y: The second integer.
    :return: Returns the greatest common divisor of the two integers.
    """

    def get_divisors(n: int) -> list[int]:
        """
        Returns a list of all divisors of n.

        :param n: The number to find divisors of.
        :return: The list of divisors of n.
        """

        return [i for i in range(1, n + 1) if n % i == 0]

    # Find the divisors of both numbers
    divisors_x = get_divisors(x)
    divisors_y = get_divisors(y)

    # Find the common divisors
    divisors_common = set(divisors_x).intersection(divisors_y)

    debug("divisors_x", divisors_x)
    debug("divisors_y", divisors_y)
    debug("divisors_common", divisors_common)

    # Return the greatest common divisor
    return max(divisors_common)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [4, 6], "result": 2},
        {"parameters": [20, 15], "result": 5},
        {"parameters": [13, 17], "result": 1},
        {"parameters": [654, 456], "result": 6},
        {"parameters": [3456, 4320], "result": 864},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = gcd(test['parameters'][0], test['parameters'][1])
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