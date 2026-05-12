# Daily challenge 2026-05-12: Character Frequency
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-12
#
# Given a string, return an object (JavaScript) or dictionary (Python) mapping each character to the number of times it appears.

from typing import TypedDict


# Challenge
def get_frequency(text: str) -> dict:
    """
    Get the frequency of each character in the string.

    :param text: The string to analyze.
    :return: Returns a dictionary mapping each character to its frequency.
    """

    result = {}

    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: dict

    unitTest: list[UnitTest] = [
        {"parameters": ["test"], "result": {"t": 2, "e": 1, "s": 1}},
        {"parameters": ["mississippi"], "result": {"m": 1, "i": 4, "s": 4, "p": 2}},
        {"parameters": ["hello world"], "result": {"h": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1}},
        {"parameters": ["She sells seashells by the seashore."], "result": {"S": 1, "h": 4, "e": 7, " ": 5, "s": 7, "l": 4, "a": 2, "b": 1, "y": 1, "t": 1, "o": 1, "r": 1, ".": 1}},
        {"parameters": ["The quick brown fox jumps over the lazy dog."], "result": {"T": 1, "h": 2, "e": 3, " ": 8, "q": 1, "u": 2, "i": 1, "c": 1, "k": 1, "b": 1, "r": 2, "o": 4, "w": 1, "n": 1, "f": 1, "x": 1, "j": 1, "m": 1, "p": 1, "s": 1, "v": 1, "t": 1, "l": 1, "a": 1, "z": 1, "y": 1, "d": 1, "g": 1, ".": 1}},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_frequency(test['parameters'][0])
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