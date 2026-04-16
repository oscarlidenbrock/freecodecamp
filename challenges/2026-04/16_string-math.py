# Daily challenge 2026-04-16: String Math
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-16
#
# Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters between the numbers.
# 
# If the count of characters separating two numbers is even, use addition.
# If it's odd, use subtraction.
# Consecutive digits form a single number.
# Operations are applied left to right.
# Ignore leading and trailing characters that aren't digits.
# 
# For example, given "3ab10c8", return 5. Add 3 and 10 to get 13 because there's an even number of characters between them. Then subtract 8 from 13 because there's an odd number of characters between the result and 8.

from typing import TypedDict


# Challenge
def do_math(input: str) -> int:
    """
    Build an arithmetic expression from the numbers in the string.
    Separator groups with even length become "+" and odd length become "-".

    :param input: A string with numbers and other characters.
    :return: The evaluated integer result.
    """

    # Ignore any leading non-digit characters before the first number.
    first_num_pos = next((i for i, c in enumerate(input) if c.isdigit()), -1)
    input_ = input[first_num_pos:]

    # Split the string into alternating groups of digits and non-digits.
    segments = [input_[0]]

    for i in range(1, len(input_)):
        char = input_[i]

        if (input_[i].isdigit() and input_[i - 1].isdigit()) or (not input_[i].isdigit() and not input_[i - 1].isdigit()):
            segments[-1] += char
        else:
            segments.append(char)

    # Normalize numeric groups so values like "09" become "9".
    for i in range(0, len(segments), 2):
        segments[i] = str(int(segments[i]))

    # Remove a trailing separator group if the string does not end in a number.
    if not segments[-1].isdigit():
        segments.pop()

    # Replace each separator group with the operator defined by its length.
    for i in range(1, len(segments), 2):
        if len(segments[i]) % 2 == 0:
            segments[i] = "+"
        else:
            segments[i] = "-"

    debug("segments operations", segments)

    # Join the pieces into a valid expression and evaluate it.
    return eval(''.join(segments))

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": ["3ab10c8"], "result": 5},
        {"parameters": ["6MINUS4"], "result": 2},
        {"parameters": ["9plus3"], "result": 12},
        {"parameters": ["5fkwo#10i#%.<>15P=@20!#B/25"], "result": 15},
        {"parameters": ["a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt"], "result": 67},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = do_math(test['parameters'][0])
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
