# Daily challenge 2025-10-30: Nth Prime
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-30
#
# A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.
# Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.

from typing import TypedDict


# Challenge
def nth_prime(n: int) -> int:
    """
    Return the nth prime number.
    :param n: The number of the prime number.
    :return: Returns the nth prime number.
    """

    def is_prime(n):
        """
        Determine if a number is prime.
        :param n: The number to check.
        :return: Returns True if the number is prime, False otherwise.
        """
        if n < 2:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        divisor = 3
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 2

        return True

    f = 0
    c = 0

    # While the number of primes is less than n, increment the counter and check if it is prime.
    while f < n:
        # Increment the counter
        c += 1

        # Check if the counter is prime
        if is_prime(c):
            # If it is prime, increment the prime counter
            f += 1

    # Return the nth prime number
    return c

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [5], "result": 11},
        {"parameters": [10], "result": 29},
        {"parameters": [16], "result": 53},
        {"parameters": [99], "result": 523},
        {"parameters": [1000], "result": 7919},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = nth_prime(test['parameters'][0])
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
