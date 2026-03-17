# Daily challenge 2025-08-25: camelCase
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-25
#
# Given a string, return its camel case version using the following rules:
# 
# Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
# The first word should be all lowercase.
# Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
# All spaces and separators should be removed.
# 

from typing import TypedDict


# Challenge
def to_camel_case(input: str) -> str:
    """
    Convert a string into camelCase.

    - Words can be separated by dashes (-) or underscores (_).
    - The first word remains lowercase.
    - Subsequent words are capitalized.

    :param input: The original string.
    :return: The camelCase version of the string.
    """

    # Normalize separators: replace dashes and underscores with spaces
    input = input.replace("-", " ")
    input = input.replace("_", " ")

    # Split the string into individual words
    words = input.split(' ')

    for w in range(len(words)):
        # Ensure each word is in lowercase
        words[w] = words[w].lower()

        # Capitalize every word except the first one
        if w > 0:
            words[w] = words[w].capitalize()

    # Combine all words without spaces to form camelCase
    result = "".join(words)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["hello world"], "result": "helloWorld"},
        {"parameters": ["HELLO WORLD"], "result": "helloWorld"},
        {"parameters": ["secret agent-X"], "result": "secretAgentX"},
        {"parameters": ["FREE cODE cAMP"], "result": "freeCodeCamp"},
        {"parameters": ["ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"], "result": "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = to_camel_case(test['parameters'][0])
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