# Daily challenge 2025-12-04: Permutation Count
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-04
#
# Given a string, return the number of distinct permutations that can be formed from its characters.
# 
# A permutation is any reordering of the characters in the string.
# Do not count duplicate permutations.
# If the string contains repeated characters, repeated arrangements should only be counted once.
# The string will contain only letters (A-Z, a-z).
# 
# For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".

from typing import TypedDict
from collections import Counter
import math


# Challenge
def count_permutations(input: str) -> int:
    """
    Counts all possible permutations or variations in a given string
    :param input: string used to count the permutations
    :return: total number of permutations
    """

    counts = Counter(input)
    n = len(input)

    d = 1
    for c in counts.values():
        d *= math.factorial(c)

    return math.factorial(n) // d


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": ["abb"], "result": 3},
        {"parameters": ["abc"], "result": 6},
        {"parameters": ["racecar"], "result": 630},
        {"parameters": ["freecodecamp"], "result": 39916800},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = count_permutations(test['parameters'][0])
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