# Daily challenge 2025-11-03: Word Counter
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-03
#
# Given a sentence string, return the number of words that are in the sentence.
# 
# Words are any sequence of non-space characters and are separated by a single space.
# 

from typing import TypedDict


# Challenge
def count_words(sentence: str) -> int:
    """
    Return the number of words in the sentence.

    :param sentence: The sentence to count words in.
    :return: Returns the number of words in the sentence.
    """

    sentence = sentence.split(" ")

    return len(sentence)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": ["Hello world"], "result": 2},
        {"parameters": ["The quick brown fox jumps over the lazy dog."], "result": 9},
        {"parameters": ["I like coding challenges!"], "result": 4},
        {"parameters": ["Complete the challenge in JavaScript and Python."], "result": 7},
        {"parameters": ["The missing semi-colon crashed the entire internet."], "result": 7},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = count_words(test['parameters'][0])
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