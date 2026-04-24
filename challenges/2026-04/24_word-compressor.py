# Daily challenge 2026-04-24: Word Compressor
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-24
#
# Given a string, return a compressed version of the string using the following rules:
# 
# The first occurrence of a word remains unchanged.
# Subsequent occurrences are replaced with the position of the first occurrence, where the first word is at position 1.
# Words are separated by a single space.
# 
# For example, given "practice makes perfect and perfect practice makes perfect", return "practice makes perfect and 3 1 2 3".

from typing import TypedDict


# Challenge
def compress(text: str) -> str:
    """
    Returns a compressed version of the input string.
    :param text: The input string.
    :return: The compressed version of the input string.
    """

    # Split the string into words
    words = text.split(" ")
    result = []

    # For each word, check if it's already in the result list. If not, add it.
    for word in words:
        if word not in result:
            result.append(word)
        else:
            result.append(str(result.index(word) + 1))

    # Return the compressed string.
    return " ".join(result)


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["practice makes perfect and perfect practice makes perfect"], "result": "practice makes perfect and 3 1 2 3"},
        {"parameters": ["hello hello hello"], "result": "hello 1 1"},
        {"parameters": ["the cat sat on the mat on which the cat sat"], "result": "the cat sat on 1 mat 4 which 1 2 3"},
        {"parameters": ["the more you know the more you realize you don't know"], "result": "the more you know 1 2 3 realize 3 don't 4"},
        {"parameters": ["lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero"], "result": "lorem ipsum dolor sit per elit donec 4 nostra libero 5 7 ligula 4 gravida at 6 vitae a 6 sodales 7 en 7 16 3 nam 13 dignissim risus 16 13 5 27 2 2 15 23 6 5 2 13 23 15 5 21 4 16 27 1 4 5 10 23 2 6 4 21 4 30 6 30 2 6 16 15 18 23 29 27 4 18 sollicitudin 5 9 5 4 10"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = compress(test['parameters'][0])
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