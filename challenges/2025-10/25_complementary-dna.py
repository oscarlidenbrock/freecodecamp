# Daily challenge 2025-10-25: Complementary DNA
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-25
#
# Given a string representing a DNA sequence, return its complementary strand using the following rules:
# 
# DNA consists of the letters "A", "C", "G", and "T".
# The letters "A" and "T" complement each other.
# The letters "C" and "G" complement each other.
# 
# For example, given "ACGT", return "TGCA".

from typing import TypedDict


# Challenge
def complementary_dna(strand: str) -> str:
    """
    Given a string representing a DNA sequence, return its complementary strand.

    :param strand: The DNA sequence.
    :return: Returns the complementary strand.
    """

    replace_grid = {"A": "T", "T": "A", "C": "G", "G": "C"}

    return "".join([replace_grid[char] for char in strand])

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["ACGT"], "result": "TGCA"},
        {"parameters": ["ATGCGTACGTTAGC"], "result": "TACGCATGCAATCG"},
        {"parameters": ["GGCTTACGATCGAAG"], "result": "CCGAATGCTAGCTTC"},
        {"parameters": ["GATCTAGCTAGGCTAGCTAG"], "result": "CTAGATCGATCCGATCGATC"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = complementary_dna(test['parameters'][0])
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