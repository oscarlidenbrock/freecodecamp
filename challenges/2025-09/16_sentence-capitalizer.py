# Daily challenge 2025-09-16: Sentence Capitalizer
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-16
#
# Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.
# 
# All other characters should be preserved.
# Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).
# 

from typing import TypedDict


# Challenge
def capitalize(paragraph: str) -> str:
    """
    Capitalize the first letter of each sentence in a paragraph.

    Sentences are assumed to be separated by '.', '?' or '!'.

    :param paragraph: Input text paragraph
    :return: Paragraph with each sentence capitalized
    """

    # Iterate over each supported sentence delimiter
    for char in [".", "?", "!"]:
        # Split the paragraph using the current delimiter
        sentences = paragraph.split(char)

        # Process each sentence fragment independently
        for i in range(len(sentences)):
            original_len = len(sentences[i])

            # Remove leading whitespace to normalize the sentence start
            sentences[i] = sentences[i].lstrip()

            # Capitalize the first character if the sentence is not empty
            if sentences[i]:
                sentences[i] = sentences[i][0].upper() + sentences[i][1:]

            # Restore original left padding to preserve formatting
            leading_spaces = original_len - len(sentences[i])
            sentences[i] = " " * leading_spaces + sentences[i]

        # Rebuild the paragraph with the same delimiter
        paragraph = char.join(sentences)

    return paragraph

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["this is a simple sentence."], "result": "This is a simple sentence."},
        {"parameters": ["hello world. how are you?"], "result": "Hello world. How are you?"},
        {"parameters": ["i did today's coding challenge... it was fun!!"], "result": "I did today's coding challenge... It was fun!!"},
        {"parameters": ["crazy!!!strange???unconventional...sentences."], "result": "Crazy!!!Strange???Unconventional...Sentences."},
        {"parameters": ["there's a space before this period . why is there a space before that period ?"], "result": "There's a space before this period . Why is there a space before that period ?"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = capitalize(test['parameters'][0])
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