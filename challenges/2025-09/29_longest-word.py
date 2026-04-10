# Daily challenge 2025-09-29: Longest Word
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-29
#
# Given a sentence, return the longest word in the sentence.
# 
# Ignore periods (.) when determining word length.
# If multiple words are ties for the longest, return the first one that occurs.
# 

from typing import TypedDict


# Challenge
def get_longest_word(sentence: str) -> str:
    """
    Return the longest word in a sentence.
    Punctuation (currently only periods) is removed before processing.

    :param sentence: Input string containing one or more words.
    :return: The longest word found in the sentence. If multiple words
             share the same maximum length, the first one is returned.
    """

    # Remove period characters from the sentence
    sentence = sentence.replace('.', '')

    # Split the sentence into individual words using spaces as separators
    words = sentence.split(' ')

    # Initialize a variable to keep track of the longest word found
    longest_word = ""

    # Iterate through each word and update the longest word when a longer one is found
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["coding is fun"], "result": "coding"},
        {"parameters": ["Coding challenges are fun and educational."], "result": "educational"},
        {"parameters": ["This sentence has multiple long words."], "result": "sentence"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_longest_word(test['parameters'][0])
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