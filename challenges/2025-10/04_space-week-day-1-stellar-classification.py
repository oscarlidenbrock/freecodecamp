# Daily challenge 2025-10-04: Space Week Day 1: Stellar Classification
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-04
#
# October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.
# For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:
# 
# "O": 30,000 K or higher
# "B": 10,000 K - 29,999 K
# "A": 7,500 K - 9,999 K
# "F": 6,000 K - 7,499 K
# "G": 5,200 K - 5,999 K
# "K": 3,700 K - 5,199 K
# "M": 0 K - 3,699 K
#
# Return the classification of the given star.
#

from typing import TypedDict


# Challenge
def classification(temp: int) -> str:
    """
    Return the stellar class that matches the given surface temperature.

    The lookup table stores the minimum Kelvin value for each class, ordered
    from the hottest stars to the coolest ones. The first threshold satisfied
    by ``temp`` determines the returned classification.

    :param temp: Surface temperature of the star in Kelvin.
    :return: Stellar classification letter for that temperature.
    """

    # Minimum temperature required for each stellar class, from hottest to
    # coolest. This order matters because the function returns the first match.
    classification = {
        "O": 30000,
        "B": 10000,
        "A": 7500,
        "F": 6000,
        "G": 5200,
        "K": 3700,
        "M": 0,
    }

    # Find the first class whose lower bound is not greater than the input
    # temperature.
    for key, value in classification.items():
        if temp >= value:
            return key

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [5778], "result": "G"},
        {"parameters": [2400], "result": "M"},
        {"parameters": [9999], "result": "A"},
        {"parameters": [3700], "result": "K"},
        {"parameters": [3699], "result": "M"},
        {"parameters": [210000], "result": "O"},
        {"parameters": [6000], "result": "F"},
        {"parameters": [11432], "result": "B"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = classification(test['parameters'][0])
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
