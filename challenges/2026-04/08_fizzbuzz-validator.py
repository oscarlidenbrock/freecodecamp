# Daily challenge 2026-04-08: FizzBuzz Validator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-08
#
# Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.
# In a valid FizzBuzz sequence:
# 
# Multiples of 3 are replaced with "Fizz".
# Multiples of 5 are replaced with "Buzz".
# Multiples of both 3 and 5 are replaced with "FizzBuzz".
# All other numbers remain as integers.
# 

from typing import TypedDict


# Challenge
def is_fizz_buzz(arr: list) -> bool:
    """
    Validate whether a sequence follows FizzBuzz rules.

    The sequence may contain integers and/or the strings "Fizz", "Buzz", and "FizzBuzz".
    At least one integer is used as an anchor to reconstruct the expected numeric sequence.

    Rules:
    - "Fizz"     → value must be divisible by 3
    - "Buzz"     → value must be divisible by 5
    - "FizzBuzz" → value must be divisible by both 3 and 5
    - Integers   → must NOT be divisible by 3 or 5

    :param arr: List containing a sequential FizzBuzz sequence (mixed integers and strings)
    :return: True if the sequence is valid, False otherwise
    """

    # Create a working copy to reconstruct the expected numeric sequence
    real_values = arr.copy()

    for v in range(len(real_values)):
        value = real_values[v]

        # Find the first integer to use as a reference point (anchor)
        if isinstance(value, int):
            # Fill preceding values based on the anchor
            temp_value_mod = -1

            for w in range(v - 1, -1, -1):
                real_values[w] = value + temp_value_mod
                temp_value_mod -= 1

            # Fill following values based on the anchor
            temp_value_mod = 1

            for w in range(v + 1, len(real_values)):
                real_values[w] = value + temp_value_mod
                temp_value_mod += 1

            break

    debug("real values", real_values)

    for v in range(len(arr)):
        value = arr[v]

        # Handle string tokens (Fizz, Buzz, FizzBuzz)
        if isinstance(value, str):
            real_value = real_values[v]
            debug("text detected", value)
            debug("real value", real_value)

            match value:
                case "Fizz":
                    # Must be divisible by 3
                    if real_value % 3 > 0:
                        debug("not divisible by 3", real_value)
                        return False

                case "Buzz":
                    # Must be divisible by 5
                    if real_value % 5 > 0:
                        debug("not divisible by 5", real_value)
                        return False

                case "FizzBuzz":
                    # Must be divisible by both 3 and 5
                    if real_value % 3 > 0 and real_value % 5 > 0:
                        debug("not divisible by 3 and 5", real_value)
                        return False

                case _:
                    # Invalid token
                    debug("invalid token", value)
                    return False

        else:
            # Integers must NOT be divisible by 3 or 5
            if not (value % 3 > 0 and value % 5 > 0):
                debug("number should not be divisible by 3 or 5", value)
                return False

    # All checks passed → valid FizzBuzz sequence
    return True

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": [[1, 2, "Fizz", 4, "Buzz"]], "result": True},
        {"parameters": [[13, 14, "FizzBuzz", 16, 17]], "result": True},
        {"parameters": [[1, 2, "Fizz", 4, 5]], "result": False},
        {"parameters": [["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]], "result": True},
        {"parameters": [[1, 2, "Fizz", "Buzz", 5]], "result": False},
        {"parameters": [[97, 98, "Buzz", "Fizz", 101, "Fizz", 103]], "result": False},
        {"parameters": [["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_fizz_buzz(test['parameters'][0])
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