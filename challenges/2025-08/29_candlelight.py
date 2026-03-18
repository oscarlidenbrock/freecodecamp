# Daily challenge 2025-08-29: Candlelight
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-29
#
# Given an integer representing the number of candles you start with, and an integer representing how many burned candles it takes to create a new one, return the number of candles you will have used after creating and burning as many as you can.
# For example, if given 7 candles and it takes 2 burned candles to make a new one:
# 
# Burn 7 candles to get 7 leftovers,
# Recycle 6 leftovers into 3 new candles (1 leftover remains),
# Burn 3 candles to get 3 more leftovers (4 total),
# Recycle 4 leftovers into 2 new candles,
# Burn 2 candles to get 2 leftovers,
# Recycle 2 leftovers into 1 new candle,
# Burn 1 candle.
# 
# You will have burned 13 total candles in the example.

from typing import TypedDict


# Challenge
def burn_candles(candles: int, leftovers_needed: int) -> int:
    """
    Calculate the total number of candles that can be burned.
    Each time a certain number of leftovers is collected, a new candle can be created.

    :param candles: Initial number of candles
    :param leftovers_needed: Number of leftovers required to make a new candle
    :return: Total number of candles burned
    """

    # Total candles burned so far (starts with the initial ones)
    result = candles

    # Current number of leftovers available to reuse
    leftovers = candles

    # Continue while we have enough leftovers to create new candles
    while leftovers >= leftovers_needed:
        # Number of new candles we can create from current leftovers
        new_candles = leftovers // leftovers_needed

        # Remaining leftovers after creating new candles, plus the new ones
        leftovers = (leftovers % leftovers_needed) + new_candles

        debug("total burned candles", result)
        debug("new candles created", new_candles)
        debug("updated leftovers", leftovers)

        # Add the newly created candles to the total burned count
        result += new_candles

    # Return the total number of candles burned
    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [7, 2], "result": 13},
        {"parameters": [10, 5], "result": 12},
        {"parameters": [20, 3], "result": 29},
        {"parameters": [17, 4], "result": 22},
        {"parameters": [2345, 3], "result": 3517},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = burn_candles(test['parameters'][0], test['parameters'][1])
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