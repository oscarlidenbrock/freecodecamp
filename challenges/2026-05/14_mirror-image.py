# Daily challenge 2026-05-14: Mirror Image
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-14
#
# Given two strings, determine if the second string is a mirror image of the first.
# A mirror image is formed by reversing the string and replacing each character with its mirror equivalent.
# 
# Symmetric characters look like themselves in a mirror:
# 
# W, T, Y, U, I, O, H, A, X, V, M, w, o, x, v, 0, 8, =, +, :, |, -, _, *, ^, !, ., and the space ( ).
# 
# Mirrored pairs swap with each other in a mirror:
#
# Character, Swaps with
# [        , ]
# {        , }
# <        , >
# b        , d
# p        , q
# (        , )
#
# If either string includes a character not in the lists above, it doesn't have mirror image that can be created from the characters.
# For example, the mirrored image of "[HOW]" is "[WOH]".

from typing import TypedDict


# Challenge
def is_mirror_image(s1, s2):
    """
    Check if the second string is a mirror image of the first.

    :param s1: The first string.
    :param s2: The second string.
    :return: Returns True if the second string is a mirror image of the first, False otherwise.
    """

    def mirror_swap(char: str) -> str:
        """
        Mirror swap.

        :param char: The character to swap.
        :return: Returns the mirrored character.
        """

        mirror_dict = {
            "[": "]",
            "{": "}",
            "<": ">",
            "b": "d",
            "p": "q",
            "(": ")",
        }

        # Add the mirrored characters to the dictionary
        mirror_dict.update({v: k for k, v in mirror_dict.items()})

        return mirror_dict.get(char, char)


    def get_mirror_image(text: str) -> str:
        """
        Get the mirror image of a string.

        :param text: A string.
        :return: Returns the mirror image of the string.
        """

        result = ""

        for char in text:
            result += mirror_swap(char)

        # Reverse the result
        result = result[::-1]

        return result

    # Get the mirror image of the first string
    mirro_s1 = get_mirror_image(s1)

    # Compare the mirror image of the first string with the second string
    return mirro_s1 == s2


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["[HOW]", "[WOH]"], "result": True},
        {"parameters": ["MOM", "MOM"], "result": True},
        {"parameters": ["vow", "wov"], "result": True},
        {"parameters": ["TIM", "TIM"], "result": False},
        {"parameters": ["{WOW}", "}WOW{"], "result": False},
        {"parameters": ["XXVII", "IIV%X"], "result": False},
        {"parameters": ["><(((*>", "<*)))><"], "result": True},
        {"parameters": ["WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()", "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW"], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_mirror_image(test['parameters'][0], test['parameters'][1])
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