# Daily challenge 2025-08-22: Message Decoder
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-22
#
# Given a secret message string, and an integer representing the number of letters that were used to shift the message to encode it, return the decoded string.
# 
# A positive number means the message was shifted forward in the alphabet.
# A negative number means the message was shifted backward in the alphabet.
# Case matters, decoded characters should retain the case of their encoded counterparts.
# Non-alphabetical characters should not get decoded.
# 

from typing import TypedDict


# Challenge
def decode(message: str, shift: int) -> str:
    """
    Encode or decode a message using the Caesar cipher.
    :param message: Message to encrypt or decrypt
    :param shift: Number of positions each character is shifted in the cipher
    :return: Encrypted or decrypted message
    """
    result = ""

    # Create strings with lowercase and uppercase letters
    dictionary_upper = "abcdefghijklmnopqrstuvwxyz"
    dictionary_lower = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Encrypt or decrypt the message
    for character in message:
        new_character = ""

        # If it is a lowercase letter
        f = dictionary_upper.find(character)

        if (f >= 0):
            # Shift the character position
            f -= shift
            if (f >= len(dictionary_upper)): f -= len(dictionary_upper)

            new_character = dictionary_upper[f]

        # If it is an uppercase letter
        f = dictionary_lower.find(character)

        if (new_character == "" and f >= 0):
            # Shift the character position
            f -= shift
            if (f >= len(dictionary_lower)): f -= len(dictionary_lower)

            new_character = dictionary_lower[f]

        # Add the character (original or shifted) to the result string
        if (new_character == ""):
            result += character
        else:
            result += new_character

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["Xlmw mw e wigvix qiwweki.", 4], "result": "This is a secret message."},
        {"parameters": ["Byffi Qilfx!", 20], "result": "Hello World!"},
        {"parameters": ["Zqd xnt njzx?", -1], "result": "Are you okay?"},
        {"parameters": ["oannLxmnLjvy", 9], "result": "freeCodeCamp"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = decode(test['parameters'][0], test['parameters'][1])
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