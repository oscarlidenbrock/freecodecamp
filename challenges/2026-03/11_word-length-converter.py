# Daily challenge 2026-03-11: Word Length Converter
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-11
#
# Given a string of words, return a new string where each word is replaced by its length.
# 
# Words in the given string will be separated by a single space
# Keep the spaces in the returned string.
# 
# For example, given "hello world", return "5 5".

from typing import TypedDict


# Challenge
def convert_words(string: str):
    """
    Return a string where each word is replaced by its length.

    :param string: The input string
    :return: A string containing the length of each word
    """
    result = ""

    # Split the string into words
    words = string.split(" ")
    debug("words", words)

    # Replace each word with its length
    for i in range(len(words)):
        words[i] = str(len(words[i]))

    # Join the words back into a single string
    result = " ".join(words)

    return resultg

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["hello world"], "result": "5 5"},
        {"parameters": ["Thanks and happy coding"], "result": "6 3 5 6"},
        {"parameters": ["The quick brown fox jumps over the lazy dog"], "result": "3 5 5 3 5 4 3 4 3"},
        {"parameters": ["Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl"], "result": "5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = convert_words(test['parameters'][0])
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