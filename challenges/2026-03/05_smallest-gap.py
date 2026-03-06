# Daily challenge 2026-03-05: Smallest Gap
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-05
#
# Given a string, return the substring between the two identical characters that have the smallest number of characters between them (smallest gap).
# 
# There will always be at least one pair of matching characters.
# The returned substring should exclude the matching characters.
# If two or more gaps are the same length, return the characters from the first one.
# 
# For example, given "ABCDAC", return "DA".
# 
# Only "A" and "C" repeat in the string.
# The number of characters between the two "A" characters is 3, and between the "C" characters is 2.
# So return the string between the two "C" characters.
# 

from typing import TypedDict


# Challenge
def smallest_gap(input: str) -> str:
    """
    Return the gap string of the one string
    :param input: the input string
    :return: the gap
    """
    gap_chars = {}

    # Search gap characters
    for i in range(len(input)):
        char = input[i]
        if input[i:].count(char) > 1: gap_chars.setdefault(i, char)

    debug("gap characters", gap_chars)

    # search the minimal len gap in gaps array and store in gaps list
    gaps = []
    min_len = len(input)

    for pos, gap_char in gap_chars.items():
        l_char = input.find(gap_char, pos)
        r_char = input.find(gap_char, pos + 1)

        gap = input[l_char + 1:r_char]
        gaps.append(gap)

        if len(gap) < min_len: min_len = len(gap)

    debug("gaps", gaps)
    debug("gap min length", min_len)

    # find the gap with len == min_len
    for gap in gaps:
        if len(gap) == min_len:
            return gap

    return ""

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["ABCDAC"], "result": "DA"},
        {"parameters": ["racecar"], "result": "e"},
        {"parameters": ["A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"], "result": "#q6e&rkf(p"},
        {"parameters": ["Hello World"], "result": ""},
        {"parameters": ["The quick brown fox jumps over the lazy dog."], "result": "fox"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print(f"Test #{n} => ", end="")

        if smallest_gap(test['parameters'][0]) == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")

            print(f"INPUT: ", test['parameters'])
            print(f"EXPECTED: ", test['result'])

            if len(debug_messages) > 0:
                print("DEBUG:")
                for msg in debug_messages:
                    print(f"", msg[0], ": ", msg[1])

            print("")


debug_messages = []


def debug(type, message):
    debug_messages.append([type, message])

test()