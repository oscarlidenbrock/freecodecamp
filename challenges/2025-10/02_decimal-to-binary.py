# Daily challenge 2025-10-02: Decimal to Binary
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-02
#
# Given a non-negative integer, return its binary representation as a string.
# A binary number uses only the digits 0 and 1 to represent any number. To convert a decimal number to binary, repeatedly divide the number by 2 and record the remainder. Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert 12 to binary:
# 12 ÷ 2 = 6 remainder 0
# 6 ÷ 2 = 3 remainder 0
# 3 ÷ 2 = 1 remainder 1
# 1 ÷ 2 = 0 remainder 1
# 
# 12 in binary is 1100.

from typing import TypedDict


# Challenge
def to_binary(decimal: int) -> str:
    """
    Convert a non-negative integer to its binary representation.

    :param decimal: Non-negative integer to convert
    :return: Binary representation as a string (without prefix)
    """

    # Use Python's built-in bin() and strip the '0b' prefix
    return bin(decimal)[2:]

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [5], "result": "101"},
        {"parameters": [12], "result": "1100"},
        {"parameters": [50], "result": "110010"},
        {"parameters": [99], "result": "1100011"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = to_binary(test['parameters'][0])
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