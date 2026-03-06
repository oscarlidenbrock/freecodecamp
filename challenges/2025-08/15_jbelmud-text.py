# Daily challenge 2025-08-15: Jbelmud Text
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-15
#
# Given a string, return a jumbled version of that string where each word is transformed using the following constraints:
# 
# The first and last letters of the words remain in place
# All letters between the first and last letter are sorted alphabetically.
# The input strings will contain no punctuation, and will be entirely lowercase.
# 

from typing import TypedDict


# Challenge
def jbelmu(text: str) -> str:
    """
    Create the jumbled version of an string
    :param text: Input string
    :return: Jumbled string
    """
    result = ""

    # get the words ot he string
    words = text.split()
    debug("words", words)

    # transform all words in jumbled version
    for i in range(len(words)):
        word = words[i]

        # Get the first character
        if len(word) > 0:
            first_char = word[0]
        else:
            first_char = ""

        # Get the last character
        if len(word) > 1:
            last_char = word[-1]
        else:
            last_char = ""

        # Get the other word excluding the first and last character
        word = word[1:-1]

        debug("first_char", first_char)
        debug("last_char", last_char)
        debug("word without first and last char", word)

        # Order alphabetically the body of the word and append the first and last character
        words[i] = first_char + "".join(sorted(word)) + last_char
        debug("jumbled word", word)

    result = " ".join(words)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["hello world"], "result": "hello wlord"},
        {"parameters": ["i love jumbled text"], "result": "i love jbelmud text"},
        {"parameters": ["freecodecamp is my favorite place to learn to code"], "result": "faccdeeemorp is my faiortve pacle to laern to cdoe"},
        {"parameters": ["the quick brown fox jumps over the lazy dog"], "result": "the qciuk borwn fox jmpus oevr the lazy dog"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = jbelmu(test['parameters'][0])
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