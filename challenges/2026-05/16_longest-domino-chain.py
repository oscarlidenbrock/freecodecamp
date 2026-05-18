# Daily challenge 2026-05-16: Longest Domino Chain
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-16
#
# Given a 2D array representing a set of dominoes, return the longest valid chain.
# 
# Each domino is a pair of numbers from 0-6, e.g. [3, 2].
# A chain is valid when the second number of each domino matches the first number of the next.
# The first number of the first domino and the second number of the last one don't need to match anything.
# Any domino can be flipped, so [3, 2] can be played as [2, 3].
# There is always exactly one longest valid chain.
# 
# For example, given [[1, 2], [4, 5], [2, 3]], return [[1, 2], [2, 3]].

from typing import TypedDict


# Challenge
def get_longest_chain(dominoes):
    """
    Return the longest valid chain of dominoes.

    :param dominoes: List of dominoes.
    :return: Returns the longest valid chain of dominoes.
    """
    longest_chain = []

    def search_chain(chain, used_indexes):
        """
        Search chain.

        :param chain: List of dominoes.
        :param used_indexes: Used indexes.
        :return: Returns the longest valid chain of dominoes.
        """
        nonlocal longest_chain

        # Save a copy when the current path is the best one found.
        if len(chain) > len(longest_chain):
            longest_chain = [domino[:] for domino in chain]

        # Only dominoes that start with this value can extend the chain.
        required_value = chain[-1][1]

        for index, domino in enumerate(dominoes):
            if index in used_indexes:
                continue

            left_value, right_value = domino

            # Try the domino in its original orientation.
            if left_value == required_value:
                used_indexes.add(index)
                search_chain(chain + [[left_value, right_value]], used_indexes)
                used_indexes.remove(index)

            # Try the domino flipped when the opposite side matches.
            if right_value == required_value and right_value != left_value:
                used_indexes.add(index)
                search_chain(chain + [[right_value, left_value]], used_indexes)
                used_indexes.remove(index)

    # Start a new search from every domino and every useful orientation.
    for index, domino in enumerate(dominoes):
        left_value, right_value = domino

        search_chain([[left_value, right_value]], {index})

        if left_value != right_value:
            search_chain([[right_value, left_value]], {index})

    return longest_chain

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [

    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_longest_chain(test['parameters'][0])
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
