# Daily challenge 2025-08-14: S  P  A  C  E  J  A  M
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-14
#
# Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.
# 
# Non-alphabetical characters should remain unchanged (except for spaces).
# 

from typing import TypedDict


# Challenge
def space_jam(input: str) -> str:
    """
    Remove all spaces from the string, insert two spaces between every character and convert all alphabetical letters to uppercase
    :param input: Input string
    :return: Result string
    """
    result = ""

    for char in input.replace(" ", "").upper():
        result += char + "  "

    result = result.rstrip()

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["freeCodeCamp"], "result": "F  R  E  E  C  O  D  E  C  A  M  P"},
        {"parameters": ["   free   Code   Camp   "], "result": "F  R  E  E  C  O  D  E  C  A  M  P"},
        {"parameters": ["Hello World?!"], "result": "H  E  L  L  O  W  O  R  L  D  ?  !"},
        {"parameters": ["C@t$ & D0g$"], "result": "C  @  T  $  &  D  0  G  $"},
        {"parameters": ["all your base"], "result": "A  L  L  Y  O  U  R  B  A  S  E"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = space_jam(test['parameters'][0])
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