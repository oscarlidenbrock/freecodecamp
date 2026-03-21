# Daily challenge 2025-09-01: Tribonacci Sequence
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-01
#
# The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.
# Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.
# 
# Your function should handle sequences of any length greater than or equal to zero.
# If the length is zero, return an empty array.
# Note that the starting numbers are part of the sequence.
# 

from typing import TypedDict


# Challenge
def tribonacci_sequence(start_sequence: list, length: int) -> list:
    """
    Generates a Tribonacci sequence based on an initial sequence and a target length.

    :param start_sequence: Initial values of the sequence (can be shorter or longer than the desired length).
    :param length: Desired number of elements in the resulting sequence.
    :return: A list containing the Tribonacci sequence up to the specified length.
    """
    sequence = start_sequence

    while len(sequence) < length:
        # Append the sum of the last three elements in the sequence
        sequence.append(sum(sequence[-3:]))

    # Return only the requested number of elements
    return sequence[:length]


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[0, 0, 1], 20], "result": [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513]},
        {"parameters": [[21, 32, 43], 1], "result": [21]},
        {"parameters": [[0, 0, 1], 0], "result": []},
        {"parameters": [[10, 20, 30], 2], "result": [10, 20]},
        {"parameters": [[10, 20, 30], 3], "result": [10, 20, 30]},
        {"parameters": [[123, 456, 789], 8], "result": [123, 456, 789, 1368, 2613, 4770, 8751, 16134]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = tribonacci_sequence(test['parameters'][0], test['parameters'][1])
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