# Daily challenge 2026-03-15: Captured Chess Pieces
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-15
#
# Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.
# In chess, you start with 16 pieces:
#
# Piece  , Abbreviation, Quantity, Value
# 
# Pawn   , "P"         , 8       , 1
# Rook   , "R"         , 2       , 5
# Knight , "N"         , 2       , 3
# Bishop , "B"         , 2       , 3
# Queen  , "Q"         , 1       , 9
# King   , "K"         , 1       , 0
# 
# The given array will only contain the abbreviations above.
# Any of the 16 pieces not included in the given array have been captured.
# Return the total value of all captured pieces, unless...
# If the King has been captured, return "Checkmate".
# 

from typing import TypedDict


# Challenge
def get_captured_value(remaining_pieces: list) -> int | str:
    """
    Calculate the total value of captured pieces based on the pieces
    remaining on the board in a chess game.

    :param remaining_pieces: List containing the remaining pieces (by symbol)
    :return: Total value of captured pieces or "Checkmate" if the king is missing
    """
    result = 0

    # Dictionary defining the initial number of each piece and its value
    # Format: "Piece": [total_count, piece_value]
    pieces = {
        "P": [8, 1],  # Pawn
        "R": [2, 5],  # Rook
        "N": [2, 3],  # Knight
        "B": [2, 3],  # Bishop
        "Q": [1, 9],  # Queen
        "K": [1, 0]   # King
    }

    # If the king is no longer on the board, the game ended by checkmate
    if "K" not in remaining_pieces:
        return "Checkmate"

    # Iterate through each piece type
    for key, piece in pieces.items():
        piece_count = piece[0]      # Initial number of that piece type
        piece_value = piece[1]      # Value assigned to that piece type

        # Count how many pieces of this type are still on the board
        remaining = remaining_pieces.count(key)

        # Determine how many pieces of this type have been captured
        captured = piece_count - remaining

        # Add the total value of captured pieces of this type
        result += (captured * piece_value)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]], "result": 8},
        {"parameters": [["P", "P", "P", "P", "P", "R", "B", "K"]], "result": 26},
        {"parameters": [["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]], "result": 16},
        {"parameters": [["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]], "result": 4},
        {"parameters": [["P", "K"]], "result": 38},
        {"parameters": [["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]], "result": 0},
        {"parameters": [["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]], "result": "Checkmate"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_captured_value(test['parameters'][0])
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