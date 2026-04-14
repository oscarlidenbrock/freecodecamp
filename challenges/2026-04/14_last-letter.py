# Daily challenge 2026-04-14: Last Letter
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-14
#
# Given a string, return the letter from the string that appears last in the alphabet.
# 
# If two or more letters tie for the last in the alphabet, return the first one.
# Ignore all non-letter characters.
# 

from typing import TypedDict


# Challenge
def get_last_letter(text: str) -> str:
    """
    Return the character whose letter is alphabetically greatest in ``text``.

    The function sorts the input case-insensitively, takes the last character
    from that ordering, and returns its first appearance from the original
    string so the original casing is preserved.

    :param text: Source text to inspect.
    :return: First occurrence of the alphabetically last character found.
    """

    # Build a case-insensitive alphabetical ordering of the input text.
    ordered_text = ''.join(sorted(text, key=str.lower))

    # The final item in the sorted string is the alphabetically greatest one.
    last_letter = ordered_text[-1]

    # Find the first matching character in the original text, ignoring case,
    # so the returned value keeps the original capitalization.
    first_coincidence = text.lower().find(last_letter.lower())

    # Return exactly one character from the original input.
    return text[first_coincidence:first_coincidence + 1]

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["world"], "result": "w"},
        {"parameters": ["Hello World"], "result": "W"},
        {"parameters": ["The quick brown fox jumped over the lazy dog."], "result": "z"},
        {"parameters": ["HeLl0"], "result": "L"},
        {"parameters": ["!#$ er@R asd fT.,> 2t0e9"], "result": "T"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_last_letter(test['parameters'][0])
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
