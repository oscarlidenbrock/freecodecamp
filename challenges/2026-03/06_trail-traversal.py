# Daily challenge 2026-03-06: Trail Traversal
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-06
#
# Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.
# The given strings will contain the values:
# 
# "C": Your current location
# "G": Your goal
# "T": Traversable parts of the trail
# "-": Untraversable parts of the map
# 
# Return a string with the moves needed to follow the trail from your location to your goal where:
# 
# 
# "R" is a move right
# "D" is a move down
# "L" is a move left
# "U" is a move up
# 
# 
# There will always be a single continuous trail, without any branching, from your current location to your goal.
# Each trail location will have a maximum of two traversable locations touching it.
#
# For example, given:
# [
#   "-CT--",
#   "--T--",
#   "--TT-",
#   "---T-",
#   "---G-"
# ]
# 
# Return "RDDRDD".

from typing import TypedDict


# Challenge
def navigate_trail(map: list) -> str:
    """
    Find the path on a map from the current position (C) to the goal (G)
    :param map: map to traverse
    :return: path to follow
    """
    result = ""

    # Find the current position (C) and the goal (G)
    c_pos = [0, 0]
    g_pos = [0, 0]

    # Search in each row (Y coordinate)
    for r in range(len(map)):
        row = map[r]
        debug("row #" + str(r), row)

        # Search in each column (X coordinate) for the characters C and G
        for c in range(len(row)):
            char = row[c]

            if char == "C": c_pos = [c, r]
            if char == "G": g_pos = [c, r]

    debug("current pos", c_pos)
    debug("goal pos", g_pos)

    goal = False

    # While the goal (G) has not been reached
    while goal == False:
        # Look for the next move, the next (T)
        next_move_result = next_move(c_pos[0], c_pos[1], map)
        next_pos = next_move_result[0]

        debug("move", str(c_pos[0]) + "," + str(c_pos[1]) + " => " + next_pos)

        # Replace the T position in the map with a - so it won't be used again
        map[c_pos[1]] = map[c_pos[1]][:(c_pos[0])] + "-" + map[c_pos[1]][(c_pos[0]+1):]

        # Update the current position
        c_pos = [next_move_result[1], next_move_result[2]]

        # If the current position is the Goal, exit the loop
        if map[c_pos[1]][c_pos[0]] == "G":
            goal = True

        # Add the move to the result
        result += next_pos

    return result

def next_move(x: int, y: int, map: list) -> list:
    """
    Find the next step (T) or the goal (G) on the map
    :param x: current x coordinate
    :param y: current y coordinate
    :param map: traversal map
    :return: the next move
    """
    if y > 0 and map[y - 1][x] in "TG": return ["U", x, y - 1] # Look up (U)
    if y < len(map) - 1 and map[y + 1][x] in "TG": return ["D", x, y + 1]  # Look down (D)
    if x > 0 and map[y][x - 1] in "TG": return ["L", x - 1, y]  # Look left (L)
    if x < len(map[y]) - 1 and map[y][x + 1] in "TG": return ["R", x + 1, y]  # Look right (R)

    return ["", x, y] # Return nothing

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [["-CT--", "--T--", "--TT-", "---T-", "---G-"]], "result": "RDDRDD"},
        {"parameters": [["-----", "--TTG", "--T--", "--T--", "CTT--"]], "result": "RRUUURR"},
        {"parameters": [["-C----", "TT----", "T-----", "TTTTT-", "----G-"]], "result": "DLDDRRRRD"},
        {"parameters": [["--------", "-CTTT---", "----T---", "---GT---", "--------"]], "result": "RRRDDL"},
        {"parameters": [["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"]], "result": "ULLLUUURRRRRRDDDR"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = navigate_trail(test['parameters'][0])
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