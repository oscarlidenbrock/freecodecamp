# Daily challenge 2026-04-04: Equation Validation
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-04
#
# Given a string representing a math equation, determine whether it is correct.
# 
# The left side may contain up to three positive integers and the operators +, -, *, and /.
# The equation will be given in the format: "number operator number = number" (with two or three numbers on the left). For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
# The right side will always be a single integer.
# 
# Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from left-to-right.

from typing import TypedDict
import re

# Challenge
def is_valid_equation(equation: str) -> bool:
    """
    Check whether a mathematical equation is valid.

    The function extracts expressions of the form:
        <operation> = <result>
    and evaluates the left-hand operation to verify that it matches the result.

    :param equation: A string containing a mathematical equation.
    :return: True if at least one valid equation is found and correctly evaluated;
             otherwise, False.
    """

    # Extract pairs of (operation, expected result) from the input string.
    # The regex ensures only basic arithmetic characters are included.
    matches = re.findall(r'([0-9+\-*/\s]+)\s?=\s?([0-9]+)', equation)

    # Evaluate each extracted operation and compare it to the expected result.
    for operation, result in matches:
        operation_result = eval(operation)
        if int(result.strip()) == operation_result:
            return True

    # No valid equation found
    return False

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["2 + 2 = 4"], "result": True},
        {"parameters": ["2 + 3 - 1 = 4"], "result": True},
        {"parameters": ["8 / 2 = 4"], "result": True},
        {"parameters": ["10 * 5 = 50"], "result": True},
        {"parameters": ["2 - 2 = 0"], "result": True},
        {"parameters": ["2 + 9 / 3 = 5"], "result": True},
        {"parameters": ["20 - 2 * 3 = 14"], "result": True},
        {"parameters": ["2 + 5 = 6"], "result": False},
        {"parameters": ["10 - 2 * 3 = 24"], "result": False},
        {"parameters": ["3 + 9 / 3 = 4"], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_valid_equation(test['parameters'][0])
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