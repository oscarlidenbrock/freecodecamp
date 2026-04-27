# Daily challenge 2026-04-26: FizzBuzz Explosion
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-26
#
# Given an integer, return the number of steps it takes to turn the word "fizzbuzz" into a string with at least the given number of "z"'s using the following rules:
# 
# Start with the string "fizzbuzz".
# Each step, apply the standard FizzBuzz rules using the letter position in the string (the first "f" is position 1).
# 
# If the letter position is divisible by 3, replace the letter with "fizz"
# If it's divisible by 5, replace the letter with "buzz"
# If it's divisible by 3 and 5, replace the letter with "fizzbuzz"
#
# So after 1 step, "fizzbuzz" turns into "fifizzzbuzzfizzzz", which has 9 "z"'s.

from typing import TypedDict


# Challenge
def explode_fizzbuzz(target_z_count: int) -> int:
    """
    Return how many expansion steps are needed for the evolving string
    to contain at least "target_z_count" occurrences of the letter "z".

    The transformation always starts from "fizzbuzz". On each step,
    every character is processed using 1-based positions:
    - positions divisible by 3 become "fizz"
    - positions divisible by 5 become "buzz"
    - positions divisible by both 3 and 5 become "fizzbuzz"
    - all other positions keep their original character

    :param target_z_count: Minimum number of "z" characters required.
    :return: Number of steps needed to reach or exceed that amount.
    """

    steps = 0
    word = "fizzbuzz"

    while word.count("z") < target_z_count:
        # Count the expansion we are about to apply.
        steps += 1

        # Build the next version of the string from left to right.
        # Positions are 1-based to match the challenge statement.
        new_word = ""
        for i, char in enumerate(word, start=1):
            if i % 3 == 0 and i % 5 == 0:
                new_word += "fizzbuzz"
            elif i % 3 == 0:
                new_word += "fizz"
            elif i % 5 == 0:
                new_word += "buzz"
            else:
                new_word += char

        # Use the expanded string for the next iteration.
        word = new_word

    return steps

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [9], "result": 1},
        {"parameters": [15], "result": 2},
        {"parameters": [51], "result": 3},
        {"parameters": [52], "result": 4},
        {"parameters": [359], "result": 5},
        {"parameters": [789], "result": 6},
        {"parameters": [54482], "result": 11},
        {"parameters": [1000000], "result": 14},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = explode_fizzbuzz(test['parameters'][0])
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
