# Daily challenge 2026-05-17: Mongo ID Date
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-17
#
# Given a MongoDB ID string, return its creation time as an ISO 8601 string.
# 
# A MongoDB ID is a 24-character hex string. The first 8 characters represent a Unix timestamp (in seconds) encoded as a base-16 integer.
# 
# For example, "6a094b50bcf86cd799439011" has a timestamp of "6a094b50" in hex, which is 1778994000 in decimal, representing a creation time of "2026-05-17T05:00:00.000Z".

from typing import TypedDict
from datetime import datetime, timezone


# Challenge
def mongo_id_to_date(mongo_id: str) -> str:
    """
    Retrive the creation time of a MongoDB ID.

    :param mongo_id: The MongoDB ID.
    :return: Returns the creation time of the MongoDB ID.
    """

    # The ObjectId timestamp is stored in the first 8 hexadecimal characters.
    timestamp_hex = mongo_id[:8]

    # Convert the hexadecimal timestamp to Unix seconds and read it as UTC.
    timestamp_seconds = int(timestamp_hex, 16)
    created_at = datetime.fromtimestamp(timestamp_seconds, timezone.utc)

    # MongoDB ObjectId timestamps only have second precision, so milliseconds are zero.
    return created_at.strftime("%Y-%m-%dT%H:%M:%S.000Z")


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["6a094b50bcf86cd799439011"], "result": "2026-05-17T05:00:00.000Z"},
        {"parameters": ["695344eb1f4a4c1123042128"], "result": "2025-12-30T03:20:11.000Z"},
        {"parameters": ["386da62df34123ac54617e56"], "result": "2000-01-01T07:01:01.000Z"},
        {"parameters": ["69f571c3d7711807afd3dd55"], "result": "2026-05-02T03:38:43.000Z"},
        {"parameters": ["68adce01c0e1144d0a90295a"], "result": "2025-08-26T15:08:49.000Z"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = mongo_id_to_date(test['parameters'][0])
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
