# Daily challenge 2026-04-13: Name Initials
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-13
#
# Given a full name as a string, return their initials.
# 
# Names to initialize are separated by a space.
# Initials should be made uppercase.
# Initials should be separated by dots.
# 
# For example, "Tommy Millwood" returns "T.M.".

from typing import TypedDict


# Challenge
def get_initials(name: str) -> str:
    """
    Generate dot-separated initials from a full name string.

    :param name: Full name as a space-separated string
    :return: String of uppercase initials, each followed by a dot
    """

    # Split the input string into individual words
    words = name.split(" ")

    # Transform each word into its uppercase initial followed by a dot
    for w in range(len(words)):
        words[w] = words[w][0].upper() + "."

    # Concatenate all initials into a single string (no spaces)
    result = "".join(words)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["Tommy Millwood"], "result": "T.M."},
        {"parameters": ["Savanna Puddlesplash"], "result": "S.P."},
        {"parameters": ["Frances Cowell Conrad"], "result": "F.C.C."},
        {"parameters": ["Dragon"], "result": "D."},
        {"parameters": ["Dorothy Vera Clump Haverstock Norris"], "result": "D.V.C.H.N."},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_initials(test['parameters'][0])
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