# Daily challenge 2025-09-04: Vowel Repeater
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-04
#
# Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear twice in a row. The third vowel should appear three times in a row, and so on.
# 
# The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
# The original vowel should keeps its case.
# Repeated vowels should be lowercase.
# All non-vowel characters should keep their original case.
# 

from typing import TypedDict


# Challenge
def repeat_vowels(text: str) -> str:
    """
    Return a new string where each vowel is repeated progressively.

    Each time a vowel appears, it is duplicated based on how many vowels
    have been encountered so far (first vowel once, second vowel twice, etc.).
    Duplicated characters are added in lowercase.

    :param text: The input string.
    :return: A new string with progressively repeated vowels.
    """
    result = ""
    c = -1

    for char in text:
        if char in "aeiouAEIOU":
            # Increment vowel counter
            c += 1

            # Add the vowel plus extra repetitions based on the counter
            result += char + (char.lower() * c)
        else:
            # Add non-vowel characters unchanged
            result += char

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["hello world"], "result": "helloo wooorld"},
        {"parameters": ["freeCodeCamp"], "result": "freeeCooodeeeeCaaaaamp"},
        {"parameters": ["AEIOU"], "result": "AEeIiiOoooUuuuu"},
        {"parameters": ["I like eating ice cream in Iceland"], "result": "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = repeat_vowels(test['parameters'][0])
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