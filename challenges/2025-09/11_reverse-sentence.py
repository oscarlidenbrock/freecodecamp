# Daily challenge 2025-09-11: Reverse Sentence
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-11
#
# Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.
# 
# In the given string, words can be separated by one or more spaces.
# The returned string should only have one space between words.
# 

from typing import TypedDict


# Challenge
def reverse_sentence(sentence: str) -> str:
    """
    Reverse the order of words in a sentence.

    Extra spaces are ignored, and the result is normalized
    to a single space between words.

    :param sentence: The input sentence.
    :return: A string with the word order reversed.
    """

    # Split the sentence into words using space as separator
    words = sentence.split(' ')

    # Filter out empty strings caused by multiple spaces
    words = [x for x in words if x != ""]

    # Reverse the order of words
    words = words[::-1]

    # Join words back into a single string with spaces
    result = " ".join(words)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["world hello"], "result": "hello world"},
        {"parameters": ["push commit git"], "result": "git commit push"},
        {"parameters": ["npm  install   apt    sudo"], "result": "sudo apt install npm"},
        {"parameters": ["import    default   function  export"], "result": "export function default import"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = reverse_sentence(test['parameters'][0])
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