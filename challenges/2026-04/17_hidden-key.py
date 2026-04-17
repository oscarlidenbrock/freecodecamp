# Daily challenge 2026-04-17: Hidden Key
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-17
#
# Welcome to the 250th daily challenge!
# Given an encoded string, decode it using an encryption key and return it.
# To find the key:
# 
# Look at all daily challenges up to today whose challenge number is a multiple of 25 (including this one).
# Take the first letter from each of those challenge titles and combine them into a string. If the title starts with a non-letter, find its first letter.
# 
# To decode the message, go over each letter in the encoded message and:
# 
# Look at the corresponding letter in the key (repeat the key if the message is longer than the key).
# Convert the key letter to its corresponding number: "A" = 1, "B" = 2, ..., "Z" = 26.
# Shift the encoded letter backward in the alphabet by that number.
# If the shift goes before "A", wrap around to "Z".
# 
# For example, if the encoded message starts with "Y" and the first key letter is "V" (22), shift "Y" back 22 places to get "C". Repeat this process for each letter to decode the full message.
# 
# Only letters are shifted, spaces are returned as-is.
# All given and returned letters are uppercase.
# 

from typing import TypedDict


# Challenge
def decode(message: str) -> str:
    """
    Decode the message using the key.
    :param message: The encoded message.
    :return: The decoded message.
    """
    key = "VLHCGMDLNH"
    result = ""
    key_index = 0

    for char in message:
        # Spaces are preserved and do not consume a key character.
        if char == " ":
            result += " "
            continue

        # Skip any non-letter characters that may appear in the key.
        while not key[key_index % len(key)].isalpha():
            key_index += 1

        key_char = key[key_index % len(key)]

        # Convert the key letter to a 1-based alphabet offset.
        shift = ord(key_char) - ord("A") + 1

        # Shift backward and wrap around the alphabet when needed.
        decoded_value = (ord(char) - ord("A") - shift) % 26
        result += chr(decoded_value + ord("A"))
        key_index += 1

    return "".join(result)



# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["YAVJYNXE"], "result": "CONGRATS"},
        {"parameters": ["YALLUT PQUMJP"], "result": "CODING LEGEND"},
        {"parameters": ["UAC DYR EISAKYM"], "result": "YOU ARE AWESOME"},
        {"parameters": ["GQMS NBMZU"], "result": "KEEP GOING"},
        {"parameters": ["W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB"], "result": "A WINNER IS A DREAMER WHO NEVER GIVES UP"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = decode(test['parameters'][0])
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
