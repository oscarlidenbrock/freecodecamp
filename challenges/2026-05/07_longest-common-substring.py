# Daily challenge 2026-05-07: Longest Common Substring
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-07
#
# Given a string, return the longest substring that appears more than once.
# 
# The substrings can overlap.
# 

from typing import TypedDict


# Challenge
def get_longest_substring(text: str) -> str:
    """
    Return the longest substring that appears more than once.

    :param text: The text to analyze.
    :return: The longest substring that appears more than once.
    """
    longest = ""

    # Sort every suffix so repeated substrings become common prefixes of
    # neighboring suffixes.
    suffixes = sorted(text[i:] for i in range(len(text)))

    for i in range(len(suffixes) - 1):
        current = suffixes[i]
        next_suffix = suffixes[i + 1]
        common_length = 0

        # Count how many starting characters both suffixes share.
        while (
            common_length < len(current)
            and common_length < len(next_suffix)
            and current[common_length] == next_suffix[common_length]
        ):
            common_length += 1

        # Keep the longest shared prefix found so far.
        if common_length > len(longest):
            longest = current[:common_length]

    return longest

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["abracadabra"], "result": "abra"},
        {"parameters": ["hello world hello"], "result": "hello"},
        {"parameters": ["mississippi"], "result": "issi"},
        {"parameters": ["ha ha ha ha ha ha ha"], "result": "ha ha ha ha ha ha"},
        {"parameters": ["the quick brown fox jumped over the lazy dog that the quick brown fox jumped over"], "result": "the quick brown fox jumped over"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_longest_substring(test['parameters'][0])
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
