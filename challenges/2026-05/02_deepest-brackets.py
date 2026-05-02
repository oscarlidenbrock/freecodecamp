# Daily challenge 2026-05-02: Deepest Brackets
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-02
#
# Given a string containing balanced brackets, return the content of the deepest nested brackets.
# 
# Brackets can be any of the three types: (), [], and {}.
# The input will always have a single deepest group.
# 
# For example, given "(hello (world))", return "world".

from typing import TypedDict

# Challenge
def get_deepest_brackets(text: str) -> str:
    """
    Get the deepest nested brackets.
    :param text: The text to parse.
    :return: The deepest nested brackets.
    """

    # Define every bracket type the parser accepts.
    opening_brackets = "([{"
    closing_brackets = ")]}"

    # Map each closing bracket to the opening bracket it must close.
    matching_opening = dict(zip(closing_brackets, opening_brackets))

    # Store open brackets and their positions so the matching text can be sliced later.
    stack: list[tuple[str, int]] = []

    # Track the deepest bracket content found while scanning the string.
    deepest_text = ""
    max_depth = 0

    # Read the string once from left to right, updating the stack as brackets open and close.
    for index, char in enumerate(text):
        # Any opening bracket increases the nesting depth, regardless of its type.
        if char in opening_brackets:
            # Keep both the bracket and its index to validate the pair and extract its content.
            stack.append((char, index))
            continue

        # Characters that are not closing brackets do not affect the current depth.
        if char not in closing_brackets:
            continue

        # A closing bracket must match the most recently opened bracket.
        opening_char, opening_index = stack.pop()

        # The challenge input is balanced, but explicit validation protects the parser contract.
        if opening_char != matching_opening[char]:
            debug("mismatched brackets", [opening_char, char])

        # The depth of the closed pair is the stack depth it had before being popped.
        current_depth = len(stack) + 1

        if current_depth > max_depth:
            # Save only the content inside the new deepest pair, excluding the brackets.
            max_depth = current_depth
            deepest_text = text[opening_index + 1:index]

    return deepest_text



# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["(hello (world))"], "result": "world"},
        {"parameters": ["[outer [inner] outer]"], "result": "inner"},
        {"parameters": ["{a{b}c{d{e}f}g}"], "result": "e"},
        {"parameters": ["[the {quick (brown [fox] jumped) over (the) lazy} dog]"], "result": "fox"},
        {"parameters": ["f[(r)e{e}C{o[(d){e(C)}a]m}]p"], "result": "C"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_deepest_brackets(test['parameters'][0])
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
