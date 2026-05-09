# Daily challenge 2025-11-08: Character Limit
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-08
#
# In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following strings based on the rules given:
# 
# "short post" if it fits within a 40-character limit.
# "long post" if it's greater than 40 characters and fits within an 80-character limit.
# "invalid post" if it's too long to fit within either limit.
# 

from typing import TypedDict


# Challenge
def can_post(message: str) -> str:
    """
    Determine if the message fits within a social media post.

    :param message: The message to check.
    :return: Returns "short post", "long post", or "invalid post" based on the message's length.
    """

    # Check if the message is too long
    if len(message) > 80:
        return "invalid post"

    # Check if the message fits within a 40-character limit
    if len(message) <= 40:
        return "short post"

    # Check if the message fits within an 80-character limit
    return "long post"


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["Hello world"], "result": "short post"},
        {"parameters": ["This is a longer message but still under eighty characters."], "result": "long post"},
        {"parameters": ["This message is too long to fit into either of the character limits for a social media post."], "result": "invalid post"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = can_post(test['parameters'][0])
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