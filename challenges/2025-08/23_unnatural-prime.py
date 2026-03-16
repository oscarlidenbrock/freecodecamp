# Daily challenge 2025-08-23: Unnatural Prime
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-23
#
# Given an integer, determine if that number is a prime number or a negative prime number.
# 
# A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
# A negative prime number is the negative version of a positive prime number.
# 1 and 0 are not considered prime numbers.
# 

from typing import TypedDict


# Challenge
def is_unnatural_prime(n: int) -> bool:
    """
    Determine whether a number is prime or the negative of a prime number.

    Since prime numbers are defined only for positive integers greater than 1,
    this function checks the absolute value of the input number.

    :param n: Integer to evaluate
    :return: True if the absolute value of n is a prime number, otherwise False
    """

    # Work with the absolute value so negative primes (e.g., -3, -5) are treated like primes
    if n < 0:
        n = n * -1

    # 0 and 1 are not prime numbers
    if n <= 1:
        return False

    # Test divisibility by every integer from 2 up to n-1
    # If any number divides n evenly, n is not prime
    for i in range(2, n):
        if n % i == 0:
            return False

    # If no divisors were found, the number is prime
    return True

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": [1], "result": False},
        {"parameters": [-1], "result": False},
        {"parameters": [19], "result": True},
        {"parameters": [-23], "result": True},
        {"parameters": [0], "result": False},
        {"parameters": [97], "result": True},
        {"parameters": [-61], "result": True},
        {"parameters": [99], "result": False},
        {"parameters": [-44], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_unnatural_prime(test['parameters'][0])
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