# Daily challenge 2026-04-27: Word Score
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-27
#
# Given a word, return its score using a standard letter-value table:
# 
# Letter, Value
# A     , 1
# B     , 2
# ...   , ...
# Z     , 26
#
# Upper and lowercase letters have the same value.
# 

from typing import TypedDict


# Challenge
def get_word_score(word: str) -> int:
    """
    Return the score of a word.
    :param word: The word.
    :return: The score of the word.
    """

    result = 0

    for char in word:
        result += ord(char.upper()) - ord("A") + 1

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": ["hi"], "result": 17},
        {"parameters": ["hello"], "result": 52},
        {"parameters": ["hippopotamus"], "result": 169},
        {"parameters": ["freeCodeCamp"], "result": 94},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_word_score(test['parameters'][0])
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