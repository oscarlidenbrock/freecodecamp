# Daily challenge 2025-09-05: IPv4 Validator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-05
#
# Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated by dots (.). Each number must satisfy the following conditions:
# 
# It is between 0 and 255 inclusive.
# It does not have leading zeros (e.g. 0 is allowed, 01 is not).
# Only numeric characters are allowed.
# 

from typing import TypedDict


# Challenge
def is_valid_ipv4(ipv4: str) -> bool:
    """
    Validate whether a string is a properly formatted IPv4 address.

    An IPv4 address must consist of exactly four numeric segments
    separated by dots (xxx.xxx.xxx.xxx). Each segment must be an
    integer between 0 and 255, with no leading zeros.

    :param ipv4: The input string representing the IP address.
    :return: True if the string is a valid IPv4 address, otherwise False.
    """

    # Split the address into its segments
    segments = ipv4.split(".")
    debug("segments", segments)

    # Ensure there are exactly four segments
    if len(segments) != 4:
        debug("check error", 1)
        return False

    # Validate each segment
    for segment in segments:
        # Ensure the segment can be converted to an integer
        try:
            value = int(segment)
        except ValueError:
            debug("check error", 2)
            return False

        # Ensure the value is within the valid IPv4 range (0–255)
        if value < 0 or value > 255:
            debug("check error", 3)
            return False

        # Ensure no leading zeros and only numeric characters
        if str(value) != segment:
            debug("check error", 4)
            return False

    # All checks passed → valid IPv4 address
    return True

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["192.168.1.1"], "result": True},
        {"parameters": ["0.0.0.0"], "result": True},
        {"parameters": ["255.01.50.111"], "result": False},
        {"parameters": ["255.00.50.111"], "result": False},
        {"parameters": ["256.101.50.115"], "result": False},
        {"parameters": ["192.168.101."], "result": False},
        {"parameters": ["192168145213"], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_valid_ipv4(test['parameters'][0])
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