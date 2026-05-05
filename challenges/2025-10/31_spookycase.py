# Daily challenge 2025-10-31: SpOoKy~CaSe
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-31
#
# Given a string representing a variable name, convert it to "spooky case" using the following constraints:
# 
# Replace all underscores (_), and hyphens (-) with a tilde (~).
# Capitalize the first letter of the string, and every other letter after that. Ignore the tilde character when counting. Make all other letters lowercase.
# 
# For example, given hello_world, return HeLlO~wOrLd.

from typing import TypedDict


# Challenge
def spookify(boo: str) -> str:
    """
    Convert a string to "spooky case".

    :param boo: The string to convert.
    :return: A string in "spooky case".
    """

    result = []
    letter_count = 0

    for char in boo.replace("_", "~").replace("-", "~"):
        if char == "~":
            result.append(char)
            continue

        if letter_count % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())

        letter_count += 1

    return "".join(result)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["hello_world"], "result": "HeLlO~wOrLd"},
        {"parameters": ["Spooky_Case"], "result": "SpOoKy~CaSe"},
        {"parameters": ["TRICK-or-TREAT"], "result": "TrIcK~oR~tReAt"},
        {"parameters": ["c_a-n_d-y_-b-o_w_l"], "result": "C~a~N~d~Y~~b~O~w~L"},
        {"parameters": ["thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts"], "result": "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = spookify(test['parameters'][0])
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
