# Daily challenge 2026-04-05: Digit Rotation Escape
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-05
#
# Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.
# A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.
# 
# Check rotation 0 (the given number) first.
# Given numbers won't contain any zeros.
# Return the first rotation number if one is found, or "none" if not.
# 

from typing import TypedDict


# Challenge
def get_rotation(number: int) -> int | str:
    """
    Returns the index of the first rotation of a number that is divisible
    by its number of digits.

    A rotation is defined as moving the first digit of the number to the end.
    The function checks all possible rotations in order.

    :param number: The input integer to evaluate
    :return: The rotation index (0-based) where the rotated number is divisible
             by its digit count, or "none" if no such rotation exists
    """

    # Convert number to string once to enable rotation operations
    rotated_number_str = str(number)

    # Iterate through all possible rotations
    for i in range(len(rotated_number_str)):
        # Convert current rotation back to integer
        rotated_number = int(rotated_number_str)

        # Check if the number is divisible by its digit count
        if rotated_number % len(rotated_number_str) == 0:
            return i

        # Perform left rotation: move first character to the end
        rotated_number_str = rotated_number_str[1:] + rotated_number_str[0]

    # No valid rotation found
    return "none"




# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [123], "result": 0},
        {"parameters": [13579], "result": 3},
        {"parameters": [24681], "result": "none"},
        {"parameters": [84138789345], "result": 6},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_rotation(test['parameters'][0])
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