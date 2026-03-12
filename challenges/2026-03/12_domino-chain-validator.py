# Daily challenge 2026-03-12: Domino Chain Validator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-12
#
# Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.
# 
# Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
# For the chain to be valid, the second number of each domino must match the first number of the next domino.
# The first number of the first domino and the last number of the last domino don't need to match anything.
# 

from typing import TypedDict

# Challenge
def is_valid_domino_chain(dominoes: list) -> bool:
    """
    Check if the domino chain is valid.
    :param dominoes: list of dominoes in the chain
    :return: True if it's a valid chain, False otherwise
    """
    for i in range(len(dominoes) - 1):
        domino = dominoes[i]
        next_domino = dominoes[i + 1]

        # Check if the second value of the current domino matches the first value of the next domino
        if domino[1] != next_domino[0]:
            return False

    # All dominoes are connected correctly, so the chain is valid
    return True

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": [[[1, 3], [3, 6], [6, 5]]], "result": True},
        {"parameters": [[[6, 2], [3, 4], [4, 1]]], "result": False},
        {"parameters": [[[2, 5], [5, 6], [5, 1]]], "result": False},
        {"parameters": [[[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]], "result": True},
        {"parameters": [[[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]]], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_valid_domino_chain(test['parameters'][0])
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