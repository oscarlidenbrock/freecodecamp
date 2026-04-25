# Daily challenge 2026-04-25: Word Decompressor
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-25
#
# Given a compressed string, return the decompressed version using the following rules:
# 
# The given string is made up of words and numbers separated by spaces.
# Leave the words unchanged.
# Replace numbers with the word at that position, where the first word is at position 1.
# 
# For example, given "practice makes perfect and 3 1 2 3", return "practice makes perfect and perfect practice makes perfect".

from typing import TypedDict


# Challenge
def decompress(text: str) -> str:
    """
    Uncompress the text.
    :param text: The compressed text.
    :return: The decompressed text.
    """

    result = []
    words = text.split(" ")

    for word in words:
        if word.isdigit():
            result.append(words[int(word)-1])
        else:
            result.append(word)

    return " ".join(result)


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["practice makes perfect and 3 1 2 3"], "result": "practice makes perfect and perfect practice makes perfect"},
        {"parameters": ["hello 1 1"], "result": "hello hello hello"},
        {"parameters": ["the cat sat on 1 mat 4 which 1 2 3"], "result": "the cat sat on the mat on which the cat sat"},
        {"parameters": ["the more you know 1 2 3 realize 3 don't 4"], "result": "the more you know the more you realize you don't know"},
        {"parameters": ["lorem ipsum dolor sit per elit donec 4 nostra libero 5 7 ligula 4 gravida at 6 vitae a 6 sodales 7 en 7 16 3 nam 13 dignissim risus 16 13 5 27 2 2 15 23 6 5 2 13 23 15 5 21 4 16 27 1 4 5 10 23 2 6 4 21 4 30 6 30 2 6 16 15 18 23 29 27 4 18 sollicitudin 5 9 5 4 10"], "result": "lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = decompress(test['parameters'][0])
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