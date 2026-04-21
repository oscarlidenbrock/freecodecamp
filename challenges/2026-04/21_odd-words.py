# Daily challenge 2026-04-21: Odd Words
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-21
#
# Given a string of words, return only the words with an odd number of letters.
# 
# Words in the given string will be separated by a single space.
# Return the words separated by a single space.
# 

from typing import TypedDict


# Challenge
def get_odd_words(text: str) -> str:
    """
    Return only the words with an odd number of letters.
    :param text: The string of words.
    :return: The words with an odd number of letters.
    """

    # Split the string into words
    words = text.split(' ')
    result = []

    for word in words:
        # Check if the word has an odd number of letters
        if len(word) % 2 == 1:
            # If it does, add it to the result list
            result.append(word)

    return ' '.join(result)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["This is a super good test"], "result": "a super"},
        {"parameters": ["one two three four"], "result": "one two three"},
        {"parameters": ["banana split sundae with rainbow sprinkles on top"], "result": "split rainbow sprinkles top"},
        {"parameters": ["The quick brown fox jumped over the lazy river"], "result": "The quick brown fox the river"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_odd_words(test['parameters'][0])
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