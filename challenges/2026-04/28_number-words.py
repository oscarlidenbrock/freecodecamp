# Daily challenge 2026-04-28: Number Words
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-28
#
# Given an integer from 0 to 99, return its English word representation.
# 
# 0 returns "zero".
# Numbers 1-19 have unique names ("one", "two", ..., "ten", "eleven", ..., "eighteen", "nineteen").
# Multiples of 10 from 20-90 have their own names ("twenty", "thirty", ..., "eighty", "ninety").
# Numbers 21-99 that are not multiples of 10 are written as two words joined by a hyphen. For example "forty-two" and "fifty-three".
# 

from typing import TypedDict


# Challenge
def get_number_words(n: int) -> str:
    """
    Return the English word representation of a number.
    :param n: The number.
    :return: The English word representation of the number.
    """

    # 0 returns "zero".
    if n == 0: return "zero"

    # Numbers 1-19 have unique names
    if n <= 19:
        numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        return numbers[n - 1]

    # Multiples of 10 from 20-90 have their own names
    if n % 10 == 0:
        numbers = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        return numbers[n // 10 - 2]

    # Numbers 21-99 that are not multiples of 10 are written as two words joined by a hyphen.
    if n % 100 != 0:
        return f"{get_number_words(int(str(n)[0]) * 10)}-{get_number_words(int(str(n)[1]))}"

    return None

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [0], "result": "zero"},
        {"parameters": [10], "result": "ten"},
        {"parameters": [19], "result": "nineteen"},
        {"parameters": [30], "result": "thirty"},
        {"parameters": [53], "result": "fifty-three"},
        {"parameters": [7], "result": "seven"},
        {"parameters": [12], "result": "twelve"},
        {"parameters": [60], "result": "sixty"},
        {"parameters": [67], "result": "sixty-seven"},
        {"parameters": [98], "result": "ninety-eight"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_number_words(test['parameters'][0])
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