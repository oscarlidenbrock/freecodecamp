# Daily challenge 2025-11-01: Signature Validation
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-01
#
# Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:
# 
# Letters in the message and secret key have these values:
# 
# a to z have values 1 to 26 respectively.
# A to Z have values 27 to 52 respectively.
# 
# 
# All other characters have no value.
# Compute the signature by taking the sum of the message plus the sum of the secret key.
# 
# For example, given the message "foo" and the secret key "bar", the signature would be 57:
# f (6) + o (15) + o (15) = 36
# b (2) + a (1) + r (18) = 21
# 36 + 21 = 57
# 
# Check if the computed signature matches the provided signature.

from typing import TypedDict


# Challenge
def verify(message: str, key: str, signature: int) -> bool:
    """
    Check if the computed signature matches the provided signature.

    :param message: The message to verify.
    :param key: The secret key to verify.
    :param signature: The signature to verify.
    :return: Returns True if the signature is valid, False otherwise.
    """

    def get_value(char):
        """
        Returns the value of a character.

        :param char: The character to get the value of.
        :return: The value of the character.
        """

        if char.islower():
            return ord(char) - ord('a') + 1
        elif char.isupper():
            return ord(char) - ord('A') + 27
        else:
            return 0

    sum = 0

    # Sum of the message
    for char in message:
        sum += get_value(char)

    # Sum of the secret key
    for char in key:
        sum += get_value(char)

    return sum == signature

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["foo", "bar", 57], "result": True},
        {"parameters": ["foo", "bar", 54], "result": False},
        {"parameters": ["freeCodeCamp", "Rocks", 238], "result": True},
        {"parameters": ["Is this valid?", "No", 210], "result": False},
        {"parameters": ["Is this valid?", "Yes", 233], "result": True},
        {"parameters": ["Check out the freeCodeCamp podcast,", "in the mobile app", 514], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = verify(test['parameters'][0], test['parameters'][1], test['parameters'][2])
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