# Daily challenge 2025-10-24: Hidden Treasure
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-24
#
# Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:
# The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.
# Each cell in the 2D array will contain one of the following values:
# 
# "-": No treasure.
# "O": A part of the treasure that has not been found.
# "X": A part of the treasure that has already been found.
#
# If the dive location has no treasure, return "Empty".
# If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".
# If the dive location finds the last unfound part of the treasure, return "Recovered".
#
# For example, given:
# [
#   [ "-", "X"],
#   [ "-", "X"],
#   [ "-", "O"]
# ]
# 
# And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure.

from typing import TypedDict


# Challenge
def dive(map: list, coordinates: list[int]) -> str:
    """
    Returns the status of the treasure after a dive.

    :param map: A lice of lists representing the map of the ocean floor.
    :param coordinates: A list with the coordinates of the dive location.
    :return: The status of the treasure after a dive.
    """

    # Debug Map
    for row in range(len(map)):
        debug("m", map[row])

    # Get the dive location
    dive_location = map[coordinates[0]][coordinates[1]]
    debug("dive_location", dive_location)

    # If dive location is "-" return "Empty"
    if dive_location == "-": return "Empty"

    # Update the map
    map[coordinates[0]][coordinates[1]] = "X"

    # Debug Map
    for row in range(len(map)):
        debug("u", map[row])


    # Determine if the treasure is found
    found = True

    for row in range(len(map)):
        if "O" in map[row]:
            found = False
            break

    if found:
        return "Recovered"
    else:
        return "Found"


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [[[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]], "result": "Recovered"},
        {"parameters": [[[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]], "result": "Empty"},
        {"parameters": [[[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]], "result": "Found"},
        {"parameters": [[[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]], "result": "Found"},
        {"parameters": [[[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]], "result": "Recovered"},
        {"parameters": [[[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]], "result": "Empty"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = dive(test['parameters'][0], test['parameters'][1])
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