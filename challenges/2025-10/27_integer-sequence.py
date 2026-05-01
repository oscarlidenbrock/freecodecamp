# Daily challenge 2025-10-27: Integer Sequence
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-27
#
# Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.
# For example, given 5, return "12345".

from typing import TypedDict


# Challenge
def sequence(n: int) -> str:
    """
    Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.

    :param n: A positive integer.
    :return: A string containing all of the integers from 1 up to, and including, the given number, in numerical order.
    """

    result = ""

    for i in range(1, n + 1):
        result += str(i)

    return result


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [5], "result": "12345"},
        {"parameters": [10], "result": "12345678910"},
        {"parameters": [1], "result": "1"},
        {"parameters": [27], "result": "123456789101112131415161718192021222324252627"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = sequence(test['parameters'][0])
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