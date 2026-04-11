# Daily challenge 2025-10-01: Binary to Decimal
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-01
#
# Given a string representing a binary number, return its decimal equivalent as a number.
# A binary number uses only the digits 0 and 1 to represent any number. To convert binary to decimal, multiply each digit by a power of 2 and add them together. Start by multiplying the rightmost digit by 2^0, the next digit to the left by 2^1, and so on. Once all digits have been multiplied by a power of 2, add the result together.
# For example, the binary number 101 equals 5 in decimal because:
# 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
# 

from typing import TypedDict


# Challenge
def to_decimal(binary: str) -> int:
    """
    Convert a binary string to its decimal (base-10) integer value.

    :param binary: String representing a binary number (e.g., "1010")
    :return: Integer representation of the binary input
    """
    return int(binary, 2)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": ["101"], "result": 5},
        {"parameters": ["1010"], "result": 10},
        {"parameters": ["10010"], "result": 18},
        {"parameters": ["1010101"], "result": 85},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = to_decimal(test['parameters'][0])
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