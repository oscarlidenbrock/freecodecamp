# Daily challenge 2025-08-27: Unorder of Operations
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-27
#
# Given an array of integers and an array of string operators, apply the operations to the numbers sequentially from left-to-right. Repeat the operations as needed until all numbers are used. Return the final result.
# For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of operations.
# 
# Valid operators are +, -, *, /, and %.
# 

from typing import TypedDict
from itertools import cycle

# Challenge
def evaluate(numbers: list, operators: list) -> int:
    """
    Evaluate a list of numbers using a corresponding list of operators in a cyclic manner.

    :param numbers: List of numbers to operate on.
    :param operators: List of operators as strings ('+', '-', '*', '/', '%').
    :return: The result of sequentially applying the operators to the numbers.
    """

    # Initialize the result with the first number and remove it from the list
    result = numbers.pop(0)

    # Create a cyclic iterator over the operators so they repeat as needed
    operators = cycle(operators)

    for number in numbers:
        # Retrieve the next operator from the cycle
        op = next(operators)

        # Apply the operator to the current result and the next number
        if op == '+':
            debug(f"{result} +", number)
            result += number
        elif op == '-':
            debug(f"{result} -", number)
            result -= number
        elif op == '*':
            debug(f"{result} *", number)
            result *= number
        elif op == '/':
            debug(f"{result} /", number)
            result /= number
        elif op == '%':
            debug(f"{result} %", number)
            result %= number

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [[5, 6, 7, 8, 9], ['+', '-']], "result": 3},
        {"parameters": [[17, 61, 40, 24, 38, 14], ['+', '%']], "result": 38},
        {"parameters": [[20, 2, 4, 24, 12, 3], ['*', '/']], "result": 60},
        {"parameters": [[11, 4, 10, 17, 2], ['*', '*', '%']], "result": 30},
        {"parameters": [[33, 11, 29, 13], ['/', '-']], "result": -2},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = evaluate(test['parameters'][0], test['parameters'][1])
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