# Daily challenge 2025-09-14: Word Frequency
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-14
#
# Given a paragraph, return an array of the three most frequently occurring words.
# 
# Words in the paragraph will be separated by spaces.
# Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
# Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
# The returned array should have all lowercase words.
# The returned array should be in descending order with the most frequently occurring word first.
# 

from typing import TypedDict


# Challenge
def get_words(paragraph: str) -> list:
    """
    Return the three most frequently occurring words in a paragraph.

    :param paragraph: A text paragraph
    :return: List of the three most frequent words in descending order of frequency
    """

    # Initialize result list (optional, can be omitted)
    result = []

    # Remove common punctuation characters to avoid splitting issues
    for char in ['.', ',', '!']:
        paragraph = paragraph.replace(char, '')

    # Convert all characters to lowercase for consistent counting
    paragraph = paragraph.lower()

    # Split the paragraph into individual words
    words = paragraph.split(' ')

    # Count the occurrences of each word
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Sort words by frequency in descending order and take the top 3
    top_words = [k for k, v in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:3]]

    return top_words

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": ["Coding in Python is fun because coding Python allows for coding in Python easily while coding"], "result": ["coding", "python", "in"]},
        {"parameters": ["I like coding. I like testing. I love debugging!"], "result": ["i", "like", "coding"]},
        {"parameters": ["Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"], "result": ["debug", "test", "deploy"]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_words(test['parameters'][0])
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