# Daily challenge 2026-03-27: Truncate the Text 2
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-27
#
# Given a string, return a new string that is truncated so that the total width of the characters does not exceed 50 units.
# Each character has a specific width:
# 
# 
# 
# Letters                    , Width
# "ilI"                      , 1
# "fjrt"                     , 2
# "abcdeghkmnopqrstuvwxyzJL" , 3
# "ABCDEFGHKMNOPQRSTUVWXYZ"  , 4
# 
# The table above includes all upper and lower case letters. Additionally:
#
# Spaces (" ") have a width of 2
# Periods (".") have a width of 1
# If the given string is 50 units or less, return the string as-is, otherwise
# Truncate the string and add three periods at the end ("...") so it's total width, including the three periods, is as close as possible to 60 units without going over.
#

from typing import TypedDict


# Challenge
def truncate_text(text: str) -> str:
    """
    Truncate a string based on visual width, not character count.

    Each character contributes a predefined width, and the total
    width must not exceed 50 units. If the limit is reached, the
    string is truncated and suffixed with "...".

    :param text: The input string to truncate.
    :return: The truncated string, with "..." appended if truncated.
    """
    result = ""

    # Mapping of character groups to their visual width
    characters_width = (
        ("ilI.", 1),
        ("fjrt ", 2),
        ("abcdeghkmnopqrstuvwxyzJL", 3),
        ("ABCDEFGHKMNOPQRSTUVWXYZ", 4)
    )

    # Current accumulated width and maximum allowed width
    w = 0
    limit = 50

    # Iterate through each character in the input text
    for char in text:
        c_w = 0

        # Determine the width of the current character
        for item in characters_width:
            if char in item[0]:
                c_w = item[1]
                break

        # Check if adding this character would exceed the limit (reserve space for "..." which has width ≈ 3)
        if w + c_w > limit - 3:
            # Append ellipsis and return the truncated result
            result += "..."
            return result
        else:
            # Append character and update accumulated width
            result += char
            w += c_w

    # If total width is within the limit, return as-is
    if w <= limit:
        return result

    # Otherwise, append ellipsis (fallback case)
    result += "..."
    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["The quick brown fox"], "result": "The quick brown f..."},
        {"parameters": ["The silky smooth sloth"], "result": truncate_text("The silky smooth sloth")},
        {"parameters": ["THE LOUD BRIGHT BIRD"], "result": "THE LOUD BRIG..."},
        {"parameters": ["The fast striped zebra"], "result": "The fast striped z..."},
        {"parameters": ["The big black bear"], "result": "The big black bear"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = truncate_text(test['parameters'][0])
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