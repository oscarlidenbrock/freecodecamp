# Daily challenge 2026-04-11: Rook and Bishop Attack
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-11
#
# Given a string for the location of a rook on a chess board, and another for the location of a bishop, determine if one piece can attack another.
# A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:
# 
# A8, B8, C8, D8, E8, F8, G8, H8
# A7, B7, C7, D7, E7, F7, G7, H7
# A6, B6, C6, D6, E6, F6, G6, H6
# A5, B5, C5, D5, E5, F5, G5, H5
# A4, B4, C4, D4, E4, F4, G4, H4
# A3, B3, C3, D3, E3, F3, G3, H3
# A2, B2, C2, D2, E2, F2, G2, H2
# A1, B1, C1, D1, E1, F1, G1, H1
#
# Rooks can move as many squares as they want in a horizontal or vertical direction.
# Bishops can move as many squares as they want in any diagonal direction.
# One piece can attack another if it can move to the location of that piece.
# 
# Return:
# 
# "rook" if the rook can attack the bishop.
# "bishop" if the bishop can attack the rook.
# "neither" if neither piece can attack one another.
# 

from typing import TypedDict


# Challenge
def rook_bishop_attack(rook: str, bishop: str) -> str:
    """
    Determine whether a rook or a bishop can capture the other piece based on their positions on a chessboard.

    :param rook: Position of the rook (e.g., "A1")
    :param bishop: Position of the bishop (e.g., "C3")
    :return: "rook" if the rook can capture the bishop,
             "bishop" if the bishop can capture the rook,
             "neither" if neither piece can capture the other
    """

    # Check if the rook can attack the bishop (same row or column)
    if rook[0] == bishop[0] or rook[1] == bishop[1]:
        return "rook"

    # Map board columns (A-H) to numeric indices for calculation
    chars = "ABCDEFGH"

    # Convert rook and bishop positions into numeric coordinates
    rook_x = chars.find(rook[0])
    rook_y = int(rook[1])
    bishop_x = chars.find(bishop[0])
    bishop_y = int(bishop[1])

    # Check if the bishop can attack the rook (same diagonal)
    if abs(bishop_x - rook_x) == abs(bishop_y - rook_y):
        return "bishop"

    # Neither piece can attack the other
    return "neither"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["A1", "A5"], "result": "rook"},
        {"parameters": ["C3", "F6"], "result": "bishop"},
        {"parameters": ["D4", "D7"], "result": "rook"},
        {"parameters": ["B7", "H1"], "result": "bishop"},
        {"parameters": ["B3", "C5"], "result": "neither"},
        {"parameters": ["G3", "E8"], "result": "neither"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = rook_bishop_attack(test['parameters'][0], test['parameters'][1])
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