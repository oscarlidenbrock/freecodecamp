# Daily challenge 2025-09-08: Acronym Builder
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-08
#
# Given a string containing one or more words, return an acronym of the words using the following constraints:
# 
# The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
# The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an, and, by, and of.
# The acronym letters should be returned in the order they are given.
# The acronym should not contain any spaces.
# 

from typing import TypedDict


# Challenge
def build_acronym(text: str) -> str:
    """
    Generate the acronym from the given text by using the first letter
    of each word, ignoring common stop words.

    :param text: The input text from which to create the acronym
    :return: The resulting acronym in uppercase
    """

    result = ""

    # Words to ignore when building the acronym
    exclude = ["a", "for", "an", "and", "by", "of"]

    # Split the text into individual words
    words = text.split(' ')

    for word in words:
        # Only consider words that start with a letter and are not in the exclusion list
        if 'A' <= word[0].upper() <= 'Z' and not word in exclude:
            # Append the uppercase first letter to the acronym
            result += word[0].upper()

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["Search Engine Optimization"], "result": "SEO"},
        {"parameters": ["Frequently Asked Questions"], "result": "FAQ"},
        {"parameters": ["National Aeronautics and Space Administration"], "result": "NASA"},
        {"parameters": ["Federal Bureau of Investigation"], "result": "FBI"},
        {"parameters": ["For your information"], "result": "FYI"},
        {"parameters": ["By the way"], "result": "BTW"},
        {"parameters": ["An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily"], "result": "AUHWPOTIMSH"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = build_acronym(test['parameters'][0])
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