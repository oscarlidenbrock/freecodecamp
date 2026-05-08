# Daily challenge 2025-11-07: Counting Cards
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-07
#
# A standard deck of playing cards has 13 unique cards in each suit. Given an integer representing the number of cards to pick from the deck, return the number of unique combinations of cards you can pick.
# 
# Order does not matter. Picking card A then card B is the same as picking card B then card A.
# 
# For example, given 52, return 1. There's only one combination of 52 cards to pick from a 52 card deck. And given 2, return 1326, There's 1326 card combinations you can end up with when picking 2 cards from the deck.

from typing import TypedDict


# Challenge
def combinations(cards: int) -> int:
    """
    Return the number of unique combinations of cards you can pick.

    :param cards: The number of cards to pick from the deck.
    :return: The number of unique combinations of cards you can pick.
    """

    # Deck size is 52
    deck_size = 52

    # Adjust the number of cards to pick if it exceeds the deck size
    cards = min(cards, deck_size - cards)
    result = 1

    # Calculate the number of unique combinations
    for card in range(1, cards + 1):
        result = result * (deck_size - cards + card) // card

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [52], "result": 1},
        {"parameters": [1], "result": 52},
        {"parameters": [2], "result": 1326},
        {"parameters": [5], "result": 2598960},
        {"parameters": [10], "result": 15820024220},
        {"parameters": [50], "result": 1326},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = combinations(test['parameters'][0])
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
