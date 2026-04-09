# Daily challenge 2026-04-09: Next Bingo Number
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-09
#
# Given a bingo number, return the next bingo number sequentially.
# A bingo number is a single letter followed by a number in its range according to this chart:
# 
# Letter , Number Range
# "B"    , 1-15
# "I"    , 16-30
# "N"    , 31-45
# "G"    , 46-60
# "O"    , 61-75
#
# For example, given "B10", return "B11", the next bingo number. If given the last bingo number, return "B1".

from typing import TypedDict


# Challenge
def get_next_bingo_number(bingo_number: str) -> str:
    """
    Compute the next bingo number in sequence.

    The sequence cycles from 1 to 75 and maps each number
    to its corresponding bingo letter:
    B (1–15), I (16–30), N (31–45), G (46–60), O (61–75).

    :param bingo_number: Current bingo number (e.g., "B12", "G58")
    :return: Next bingo number in sequence (e.g., "B13", "G59")
    """

    # Mapping of upper bounds to their corresponding bingo letters
    bingo_letters = {
        15: "B",
        30: "I",
        45: "N",
        60: "G",
        75: "O"
    }

    # Extract the letter and numeric value from the input
    bingo_number_letter = bingo_number[0]
    bingo_number_value = int(bingo_number[-2:])

    # Increment the number, wrapping around after 75
    next_number = bingo_number_value + 1
    if next_number > 75:
        next_number = 1

    # Determine the corresponding letter for the next number
    next_letter = ""
    for upper_bound in bingo_letters:
        if next_number <= upper_bound:
            next_letter = bingo_letters[upper_bound]
            break

    # Construct the resulting bingo number string
    result = next_letter + str(next_number)

    return result
# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["B10"], "result": "B11"},
        {"parameters": ["N33"], "result": "N34"},
        {"parameters": ["I30"], "result": "N31"},
        {"parameters": ["G60"], "result": "O61"},
        {"parameters": ["O75"], "result": "B1"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_next_bingo_number(test['parameters'][0])
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