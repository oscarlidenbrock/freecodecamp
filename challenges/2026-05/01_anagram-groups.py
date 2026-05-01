# Daily challenge 2026-05-01: Anagram Groups
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-01
#
# Given an array of words, return a 2d array of the words grouped into anagrams.
# 
# Words are anagrams if they contain the same letters in any order.
# Each word belongs to exactly one group.
# Return order doesn't matter.
# 
# For example, given ["listen", "silent", "hello", "enlist", "world"], return [["listen", "silent", "enlist"], ["hello"], ["world"]].

from typing import TypedDict
from collections import Counter
import re

# Challenge
def group_anagrams(words: list) -> list:
    """
    Group anagrams.
    :param words: A list of words.
    :return: Returns a list of lists containing the anagrams.
    """

    def is_anagram(string1: str, string2: str) -> bool:
        """
        Check if two strings are anagrams.
        :param string1: First string.
        :param string2: Second string.
        :return: Returns True if the strings are anagrams, otherwise False.
        """
        s1 = re.sub(r'[^a-z]', '', string1.lower())
        s2 = re.sub(r'[^a-z]', '', string2.lower())

        return Counter(s1) == Counter(s2)

    anagrams = {}

    # For each word, check if it is an anagram of any other word
    for word in words:
        found = False

        for anagram in anagrams:
            # If the word is an anagram of another word, add it to the list
            if is_anagram(word, anagram):
                anagrams[anagram].append(word)
                found = True
                break

        if not found:
            # If the word is not an anagram of any other word, create a new list
            anagrams[word] = [word]

    # Create result list
    result = []
    for anagram in anagrams:
        result.append(anagrams[anagram])

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [["listen", "silent", "hello", "enlist", "world"]], "result": [["listen", "silent", "enlist"], ["hello"], ["world"]] },
        {"parameters": [["eat", "tea", "tan", "ate", "nat", "bat"]], "result": [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] },
        {"parameters": [["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"]], "result": [['care', 'race', 'acre'], ['pots', 'stop', 'tops', 'opts', 'post', 'spot'], ['evil', 'vile', 'live', 'veil']] },
        {"parameters": [["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"]], "result": [['algorithms', 'logarithms'], ['education', 'cautioned', 'auctioned'], ['triangle', 'integral', 'alerting', 'relating']] }
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = group_anagrams(test['parameters'][0])
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