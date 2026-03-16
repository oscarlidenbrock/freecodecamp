# Daily challenge 2025-08-24: Character Battle
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-24
#
# Given two strings representing your army and an opposing army, each character from your army battles the character at the same position from the opposing army using the following rules:
# 
# Characters a-z have a strength of 1-26, respectively.
# Characters A-Z have a strength of 27-52, respectively.
# Digits 0-9 have a strength of their face value.
# All other characters have a value of zero.
# Each character can only fight one battle.
# 
# For each battle, the stronger character wins. The army with more victories, wins the war. Return the following values:
# 
# "Opponent retreated" if your army has more characters than the opposing army.
# "We retreated" if the opposing army has more characters than yours.
# "We won" if your army won more battles.
# "We lost" if the opposing army won more battles.
# "It was a tie" if both armies won the same number of battles.
# 

from typing import TypedDict


# Challenge
def battle(my_army: str, opposing_army: str) -> str:
    """
    Simulate a battle between two armies represented as strings.

    Each character represents a unit. Units fight in pairs based on their
    position in the string. The unit with the higher value wins the duel.

    If the armies have different sizes, the smaller one retreats before battle.

    :param my_army: String representing my army
    :param opposing_army: String representing the enemy army
    :return: The result of the battle
    """

    # If your army has more characters than the opposing army...
    if len(my_army) > len(opposing_army):
        return "Opponent retreated"

    # If the opposing army has more characters than yours...
    if len(opposing_army) > len(my_army):
        return "We retreated"

    # Battle score: positive means we are winning, negative means we are losing
    result = 0

    for c in range(len(my_army)):
        my_value = character_value(my_army[c])
        enemy_value = character_value(opposing_army[c])

        if my_value > enemy_value:
            # Our unit wins the duel
            result += 1
        elif enemy_value > my_value:
            # Enemy unit wins the duel
            result -= 1
        else:
            # Both units have the same value (draw)
            result += 0

    # If your army won more battles...
    if result > 0:
       return "We won"

    # If the opposing army won more battles...
    if result < 0:
       return "We lost"

    # If both armies won the same number of battles...
    return "It was a tie"

def character_value(character: str) -> int:
    """
    Return the numeric value assigned to a character in the battle system.

    Value rules:
    - 'a' to 'z' → 1 to 26
    - 'A' to 'Z' → 27 to 52
    - '0' to '9' → numeric value of the digit
    - Any other character → 0

    :param character: A single character representing a unit
    :return: The numeric value associated with the character
    """

    ascii_value = ord(character[0])

    # Lowercase letters (a–z) → values 1–26
    if ascii_value >= 97 and ascii_value <= 122:
        return ascii_value - 96

    # Uppercase letters (A–Z) → values 27–52
    if ascii_value >= 65 and ascii_value <= 90:
        return ascii_value - 38

    # Numeric characters (0–9) → their integer value
    if ascii_value >= 48 and ascii_value <= 57:
        return int(character[0])

    # Any other character has no battle value
    return 0

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["Hello", "World"], "result": "We lost"},
        {"parameters": ["pizza", "salad"], "result": "We won"},
        {"parameters": ["C@T5", "D0G$"], "result": "We won"},
        {"parameters": ["kn!ght", "orc"], "result": "Opponent retreated"},
        {"parameters": ["PC", "Mac"], "result": "We retreated"},
        {"parameters": ["Wizards", "Dragons"], "result": "It was a tie"},
        {"parameters": ["Mr. Smith", "Dr. Jones"], "result": "It was a tie"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = battle(test['parameters'][0], test['parameters'][1])
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