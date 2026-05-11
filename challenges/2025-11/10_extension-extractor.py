# Daily challenge 2025-11-10: Extension Extractor
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-10
#
# Given a string representing a filename, return the extension of the file.
# 
# The extension is the part of the filename that comes after the last period (.).
# If the filename does not contain a period or ends with a period, return "none".
# The extension should be returned as-is, preserving case.
# 

from typing import TypedDict


# Challenge
def get_extension(filename: str) -> str:
    """
    Return the extension of the file.

    :param filename: The filename.
    :return: The extension of the file.
    """

    segments = filename.split(".")

    if len(segments) == 1 or segments[-1] == "":
        return "none"
    else:
        return segments[-1]

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["document.txt"], "result": "txt"},
        {"parameters": ["README"], "result": "none"},
        {"parameters": ["image.PNG"], "result": "PNG"},
        {"parameters": [".gitignore"], "result": "gitignore"},
        {"parameters": ["archive.tar.gz"], "result": "gz"},
        {"parameters": ["final.draft."], "result": "none"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_extension(test['parameters'][0])
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