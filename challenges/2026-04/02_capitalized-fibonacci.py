# Daily challenge 2026-04-02: Capitalized Fibonacci
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-02
#
# Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
# 
# The first character is at index 0.
# If the index of non-letter characters is a Fibonacci number, leave it unchanged.
# 

from typing import TypedDict


# Challenge
def capitalize_fibonacci(text: str) -> str:
    """
    Returns a new string where alphabetic characters are uppercased
    if their index matches a Fibonacci number; otherwise they are lowercased.

    :param text: Input string to transform
    :return: Transformed string based on Fibonacci index positions
    """

    # Initialize Fibonacci sequence with the first two indices (0-based indexing)
    fibonacci = [0, 1]

    # Extend the sequence until the largest value covers the text length
    while max(fibonacci) < len(text):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    # Debug: output generated Fibonacci indices
    debug("fibonacci sequence", fibonacci)

    # Accumulate the resulting transformed string
    result = ""

    # Iterate over each character using its index
    for c in range(len(text)):
        char = text[c]

        # Check if the character is an alphabetic letter (case-insensitive)
        if "a" <= char.lower() <= "z":
            if c in fibonacci:
                # Convert to uppercase if index is in Fibonacci sequence
                result += char.upper()
                debug("upper char " + char.upper(), c)
            else:
                # Convert to lowercase if index is not in Fibonacci sequence
                result += char.lower()
        else:
            # Preserve non-alphabetic characters as-is
            result += char

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["hello world"], "result": "HELLo woRld"},
        {"parameters": ["HELLO WORLD"], "result": "HELLo woRld"},
        {"parameters": ["hello, world!"], "result": "HELLo, wOrld!"},
        {"parameters": ["The quick brown fox jumped over the lazy dog."], "result": "THE qUicK broWn fox jUmped over thE lazy dog."},
        {"parameters": ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl."], "result": "LOREm ipSum dOlor sit amet, consecTetur adipiscing elit. proin pulvinar ex nibh, vel ullaMcorper ligula egestas quis. integer tincidunt fringillA accumsan. integer et metus placerat, gravida felis at, pellentesque nisl."},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = capitalize_fibonacci(test['parameters'][0])
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