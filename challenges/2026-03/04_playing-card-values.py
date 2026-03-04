# Daily challenge 2026-03-04: Playing Card Values
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-04
#
# Given an array of playing cards, return a new array with the numeric value of each card.
# Card Values:
# 
# An Ace ("A") has a value of 1.
# Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
# Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
# 
# Suits:
# 
# Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
# 
# Card Format:
# 
# Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.
# 

from typing import TypedDict


# Challenge
def card_values(cards: list) -> list:
    """
    Return an array with the numeric value of each card given in cards array
    :param cards:
    :return: array with numeric values
    """
    result = []
    cardValue = 0

    for card in cards:
        # remove suit from card string (S/C/D/H)
        cardValue = card[:-1]

        # change card values (Ace = 1, J/Q/K = 10)
        match cardValue:
            case "A": cardValue = 1
            case "J": cardValue = 10
            case "Q": cardValue = 10
            case "K": cardValue = 10
            case _: cardValue = int(cardValue)

        result.append(cardValue)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [["3H", "4D", "5S"]], "result": [3, 4, 5]},
        {"parameters": [["AS", "10S", "10H", "6D", "7D"]], "result": [1, 10, 10, 6, 7]},
        {"parameters": [["8D", "QS", "2H", "JC", "9C"]], "result": [8, 10, 2, 10, 9]},
        {"parameters": [["AS", "KS"]], "result": [1, 10]},
        {"parameters": [["10H", "JH", "QH", "KH", "AH"]], "result": [10, 10, 10, 10, 1]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if card_values(test['parameters'][0]) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")

test()